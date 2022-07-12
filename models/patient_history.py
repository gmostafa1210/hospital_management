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
    test_line_ids = fields.One2many('hospital.history.test.line', 'patient_history_id', string='Test Line')
    madicine_line_ids = fields.One2many('hospital.history.madicine.line', 'patient_history_id', string='Madicine Line')

    def action_done(self):
        self.state = 'done'

    def action_pending(self):
        self.state = 'pending'


class HospitalHistoryTestLine(models.Model):
    _name = 'hospital.history.test.line'
    _description = 'Patient History Test Line Master Description.'
    _rec_name = 'test_id'

    test_id = fields.Many2one('hospital.test', string='Test Name')
    test_copy = fields.Binary(string='Test Copy')
    result = fields.Text(string='Remarks')
    date = fields.Date(string='Test Date', default=date.today())
    patient_history_id = fields.Many2one('hospital.patient.history', string='Patient History')


class HospitalHistoryMadicineLine(models.Model):
    _name = 'hospital.history.madicine.line'
    _description = 'Patient History Madicine Line Master Description.'
    _rec_name = 'madicine_id'

    madicine_id = fields.Many2one('hospital.madicine', string='Madicine Name')
    mg_ml = fields.Float(string='MG/ML')
    days = fields.Integer(string='Days')
    quantity = fields.Integer(string='Quantity')
    when_to_take = fields.Selection([
            ('before', 'Before Meal'), ('after', 'After Meal')], string='When to Take')
    patient_history_id = fields.Many2one('hospital.patient.history', string='Patient History')