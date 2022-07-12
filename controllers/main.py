# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class HospitalAppointment(http.Controller):

    @http.route('/appointment_form', type="http", auth="public", website=True)
    def take_appointment(self, **kw):
        # patient_history_rec = request.env['hospital.patient.history'].sudo().search([])
        return http.request.render('hospital_management.take_appointment_form', {})

    @http.route('/create/appointment', type="http", auth="public", website=True)
    def create_appointment_form(self, **kw):
        # request.env['hospital.patient.history'].sudo().create(kw)
        return request.render("hospital_management.patient_thanks", {})