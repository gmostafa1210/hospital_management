# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    def domain_set(self):
        doc_list = []
        res_obj = self.env['res.users'].search([])
        for res in res_obj:
            if res.doctor_id:
                doc_list.append(res.doctor_id.id)
        return [('id', 'not in', doc_list)]

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', domain=domain_set)

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        if self.doctor_id:
            self.login = self.doctor_id.email
            if self.doctor_id.last_name:
                self.name = self.doctor_id.first_name + ' ' + self.doctor_id.last_name
            else:
                self.name = self.doctor_id.first_name

