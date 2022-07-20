# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class HospitalAppointment(http.Controller):

    @http.route('/appointment_form', type="http", auth="public", website=True)
    def take_appointment(self, **kw):
        return http.request.render('hospital_management.take_appointment_form', {})

    @http.route('/create/patient', type="http", auth="public", website=True)
    def create_patient(self, **kw):
        if kw:
            phone_number = kw['phone']
            patient_rec = request.env['hospital.patient'].sudo().search([('phone', '=', phone_number)])
            hospital_rec = request.env['hospital.hospital'].sudo().search([])
            department_rec = request.env['hospital.department'].sudo().search([])
            doctor_rec = request.env['hospital.doctor'].sudo().search([])
            if not patient_rec:
                request.env['hospital.patient'].sudo().create(kw)
            new_patient_rec = request.env['hospital.patient'].sudo().search([('phone', '=', phone_number)])
            return http.request.render('hospital_management.patient_appointment', 
                    {'new_patient_rec': new_patient_rec, 'hospital_rec': hospital_rec,
                    'department_rec': department_rec, 'doctor_rec': doctor_rec})

    @http.route('/create/appointment', type="http", auth="public", website=True)
    def create_appointment(self, **kw):
        history_id = request.env['hospital.patient.history'].sudo().create(kw)
        return request.render("hospital_management.patient_thanks", {'history_id': history_id})

    @http.route(['/change/hospital'], type='json', auth="public", website=True, csrf=False)
    def hospital_change(self, hospital_id):
        department_list = request.env['hospital.hospital'].sudo().search([('id', '=', hospital_id)]).department_ids.ids
        department_ids = request.env['hospital.department'].sudo().search_read([('id', 'in', department_list)])
        return department_ids

    @http.route(['/change/department'], type='json', auth="public", website=True, csrf=False)
    def department_change(self, department_id,hospital_id):
        doctor_ids = request.env['hospital.doctor'].sudo().search_read([('department_id', '=', department_id), ('hospital_id', '=', hospital_id)])
        return doctor_ids
