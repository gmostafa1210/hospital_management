# -*- coding: utf-8 -*-

from ctypes.wintypes import MSG
from odoo import models, api, fields, _
from datetime import date


class HospitalMadicine(models.Model):
    _name = 'hospital.madicine'
    _description = 'Patient Madicine Master Description.'

    name = fields.Char(string='Madicine Name', required=True)
    mg_ml = fields.Float(string='MG/ML')
    days = fields.Integer(string='Days')
    quantity = fields.Integer(string='Quantity')
    when_to_take = fields.Selection([
            ('before', 'Before Meal'), ('after', 'After Meal')], string='When to Take')
    patient_history_id = fields.Many2one('hospital.patient.history', string='Patient History')
