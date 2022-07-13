# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class HospitalAppointment(http.Controller):

    @http.route('/appointment_form', type="http", auth="public", website=True)
    def take_appointment(self, **kw):
        # patient_history_rec = request.env['hospital.patient.history'].sudo().search([])
        return http.request.render('hospital_management.take_appointment_form', {})

    @http.route('/create/appointment', type="http", auth="public", website=True)
    def create_patient(self, **kw):
        if kw:
            phone_number = kw['phone']
            patient_rec = request.env['hospital.patient'].sudo().search([('phone', '=', phone_number)])
        # request.env['hospital.patient'].sudo().create(kw)
        if patient_rec:
            print("##################Patient Already Exist", patient_rec)
        else:
            request.env['hospital.patient'].sudo().create(kw)
        return request.render("hospital_management.patient_thanks", {})