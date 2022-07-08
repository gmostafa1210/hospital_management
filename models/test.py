# -*- coding: utf-8 -*-

from ctypes.wintypes import MSG
from odoo import models, api, fields, _
from datetime import date


class HospitalTest(models.Model):
    _name = 'hospital.test'
    _description = 'Patient Test Master Description.'

    name = fields.Char(string='Test Name')
    test_copy = fields.Binary(string='Test Copy')
    result = fields.Text(string='Remarks')
    date = fields.Date(string='Test Date', default=date.today())