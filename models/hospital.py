# -*- coding: utf-8 -*-

from odoo import models, api, fields, _


class HospitalHospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'Hospital Master Description.'

    name = fields.Char(string='Hospital Name', required=True)
    hospital_code = fields.Char(string='Hospital Code', required=True, 
            copy=False, readonly=True, index=True, default=lambda self: _('New'))
    patient_capacity = fields.Integer(string='Patient Capacity')
    available_doctor = fields.Integer(string='Available Doctor')
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    doctor_ids = fields.One2many('hospital.doctor', 'hospital_id', string='Doctor List')
    department_ids = fields.Many2many('hospital.department', string='Available Departments')

    @api.model
    def create(self, values):
        if values.get('hospital_code', _('New')) == _('New'):
            values['hospital_code'] = self.env['ir.sequence'].next_by_code('hospital.hospital.sequence') or _('New')
        return super(HospitalHospital, self).create(values)
