# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class HospitalAppointment(http.Controller):

    @http.route('/create/appointment_form', type="http", auth="public", website=True)
    def take_appointment_form(self, **kw):
        patient_history_rec = request.env['hospital.patient.history'].sudo().search([])
        return http.request.render('om_hospital.take_appointment_form', {})

    @http.route('/create/appointment_form', type="http", auth="public", website=True)
    def create_appointment_form(self, **kw):
        request.env['hospital.patient.history'].sudo().create(kw)
        return request.render("om_hospital.patient_thanks", {})