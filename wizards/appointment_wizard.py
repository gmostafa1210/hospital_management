# -*- coding: utf-8 -*-

from odoo import models, fields, _


class HospitalAppointmentWizard(models.TransientModel):
    _name = 'hospital.appointment.wizard'
    _description = 'Patient Appointment Wizard Master Description.'

    appointment_id = fields.Many2one('hospital.patient.history', string='Appointment Code')

    def action_view_history(self):
        """
        This function will search patient history by appointment code by wizard.
        """
        self.ensure_one()
        return {
            'name': _('Patient History'),
            'view_mode': 'form',
            'res_model': 'hospital.patient.history',
            'type': 'ir.actions.act_window',
            'res_id': self.appointment_id.id,
        }