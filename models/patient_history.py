# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date


class HospitalPatientHistory(models.Model):
    _name = 'hospital.patient.history'
    _description = 'Patient History Master Description.'

    date = fields.Date(string='Date', default=date.today())
    patient_id = fields.Many2one('hospital.patient', string='Patient Name')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name')
    medicine_ids = fields.One2many('hospital.madicine', 'history_id', string='Madicine')
