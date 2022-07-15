# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalMadicine(models.Model):
    _name = 'hospital.madicine'
    _description = 'Patient Madicine Master Description.'

    name = fields.Char(string='Madicine Name', required=True)
    mg_ml = fields.Float(string='MG/ML')
