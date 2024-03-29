# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date


class HospitalPatientHistory(models.Model):
    _name = 'hospital.patient.history'
    _description = 'Patient History Master Description.'
    _rec_name = 'appointment_code'

    date = fields.Date(string='Date', default=date.today())
    patient_id = fields.Many2one('hospital.patient', string='Patient Name')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name')
    appointment_code = fields.Char(string='Appointment Code', required=True, 
            copy=False, readonly=True, index=True, default=lambda self: _('New'))
    department_id = fields.Many2one('hospital.department', string='Department')
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

    def button_redrict_patient_history(self):
        """
        This function will redrict patient history.
        """
        self.ensure_one()
        return {
            'name': _('Patient History'),
            'view_mode': 'tree,form',
            'res_model': 'hospital.patient.history',
            'type': 'ir.actions.act_window',
            'domain': [('patient_id', '=', self.patient_id.id)],
        }

    @api.model
    def create(self, values):
        if values.get('appointment_code', _('New')) == _('New'):
            values['appointment_code'] = self.env['ir.sequence'].next_by_code('hospital.patient.history.sequence') or _('New')
        return super(HospitalPatientHistory, self).create(values)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        This function will search the appointment by appointment code and patient name.
        """
        args = args or []
        domain = []
        if name:
            domain = ['|', ('patient_id', operator, name), ('appointment_code', operator, name)] 
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)


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

    @api.onchange('madicine_id')
    def onchange_madicine_id(self):
        if self.madicine_id and self.madicine_id.mg_ml:
            self.mg_ml = self.madicine_id.mg_ml