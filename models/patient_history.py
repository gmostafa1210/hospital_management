# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date


class HospitalPatientHistory(models.Model):
    _name = 'hospital.patient.history'
    _description = 'Patient History Master Description.'
    _rec_name = 'patient_id'

    date = fields.Date(string='Date', default=date.today())
    patient_id = fields.Many2one('hospital.patient', string='Patient Name')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name')
    hospital_id = fields.Many2one('hospital.hospital', string='Hospital Name', related='doctor_id.hospital_id')
    symptoms = fields.Text(string='Symptoms')  
    state = fields.Selection([
            ('pending', 'Pending'), ('done', 'Done')], string='State', default='pending')
    medicine_ids = fields.One2many('hospital.madicine', 'patient_history_id', string='Madicine')
    test_ids = fields.Many2many('hospital.test', string='Test')

    def action_done(self):
        self.state = 'done'

    def action_pending(self):
        self.state = 'pending'
