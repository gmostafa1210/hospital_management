# -*- coding: utf-8 -*-

from odoo import models, api, fields


class HospitalHospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'Hospital Master Description.'

    first_name = fields.Char(string='First Name', required=True)
