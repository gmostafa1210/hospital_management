# -*- coding: utf-8 -*-

from ctypes.wintypes import MSG
from odoo import models, api, fields, _
from datetime import date


class HospitalMadicine(models.Model):
    _name = 'hospital.madicine'
    _description = 'Patient Madicine Master Description.'

    name = fields.Char(string='Madicine Name', required=True)
    mg_ml = fields.Float(string='MG/ML')
