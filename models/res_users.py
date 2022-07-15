# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        if self.doctor_id:
            self.login = self.doctor_id.email
            self.name = self.doctor_id.first_name + ' ' + self.doctor_id.last_name or ''

