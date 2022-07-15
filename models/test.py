# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalTest(models.Model):
    _name = 'hospital.test'
    _description = 'Patient Test Master Description.'

    name = fields.Char(string='Test Name', required=True)