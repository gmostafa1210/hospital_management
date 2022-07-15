# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Patient Department Master Description.'

    name = fields.Char(string='Department Name', required=True)