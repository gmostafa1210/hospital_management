# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date


class HospitalPatientHistory(models.Model):
    _name = 'hospital.patient.history'
    _description = 'Patient History Master Description.'

    patient_id = fields.Many2one(
        'hospital.patient', string='Patient Name')
    date = fields.Date(string='Date', default=date.today())
