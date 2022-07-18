# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from datetime import date
from odoo.exceptions import UserError
import re


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Master Description.'
    _rec_name = 'first_name'
    _sql_constraints = [
        ('phone_unique', 'unique(phone)', 'Phone number already exists!'),
        ('email_unique', 'unique(email)', 'Email already exists!'),
        ('nid_unique', 'unique(nid)', 'NID already exists!'),
    ]

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Name', compute='_get_full_name')
    doctor_code = fields.Char(string='Doctor Code', required=True, 
            copy=False, readonly=True, index=True, default=lambda self: _('New'))
    email = fields.Char(string='Email', required=True, copy=False)
    phone = fields.Char(string='Phone', required=True, copy=False)
    nid = fields.Char(string='NID Number', copy=False)
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age', compute='_get_age')
    gender = fields.Selection([('male', 'Male'), 
            ('female', 'Female')], string='Gender', default='male')
    history_ids = fields.One2many(
            'hospital.patient.history', 'doctor_id', string='Patient History', required=True)   
    img = fields.Binary(string='Profile Image', attachment=True)
    address = fields.Text(string='Address')
    hospital_id = fields.Many2one('hospital.hospital', string='Assigned Hospital', required=True)
    department_id = fields.Many2one('hospital.department', string='Department', required=True) 

    def full_name(self):
        """
        This function will compute full name.
        """
        first_name = ''
        last_name = ''
        if self.first_name:
            first_name = self.first_name
        if self.last_name:
            last_name = self.last_name
        return first_name + ' ' + last_name
        
    def _get_full_name(self):
        """
        This function will return full name.
        """
        for item in self:
            item.name = item.full_name()

    def _get_age(self):
        """
        This function will calculate the age from the dob. 
        """
        for record in self:
            if record.dob:
                today = date.today()
                if today.strftime("%m%d") >= record.dob.strftime("%m%d"):
                    record['age'] = today.year - record.dob.year
                else:
                    record['age'] = today.year - record.dob.year - 1
            else:
                record['age'] = 0

    @api.constrains('dob', 'phone', 'email')
    def _check_validity(self):
        """
        This function will check the validity of dob, phone, email.
        """
        for record in self:
            if record.dob and record.dob >= date.today():
                raise UserError(_("Invalid DOB!"))
            if record.phone:
                if len(record.phone) != 11 or not record.phone.isnumeric() or record.phone[0:2] != '01':
                    raise UserError(_("Not a valid phone number."))
            if record.email:
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
                if match == None:
                    raise UserError(_('Not a valid email!'))

    @api.model
    def create(self, values):
        if values.get('doctor_code', _('New')) == _('New'):
            values['doctor_code'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or _('New')
        return super(HospitalDoctor, self).create(values)

    def button_redirect_patient_list(self):
        """
        This function will redrict patient list.
        """
        self.ensure_one()
        return {
            'name': _('Patient List'),
            'view_mode': 'tree,form',
            'res_model': 'hospital.patient.history',
            'type': 'ir.actions.act_window',
            'domain': [('doctor_id', '=', self.id)],
            'context': {'search_default_get_pending_patient': 1},
        }

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """
        This function will search the doctor by name, code and phone number.
        """
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', '|', ('first_name', operator, name), ('last_name', operator, name), ('phone', operator, name), ('doctor_code', operator, name)] 
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    def name_get(self):
        """
        This function will return the full name of the doctor with doctor code.
        """
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s' % (rec.doctor_code, rec.full_name())))
        return result

    @api.onchange('hospital_id')
    def onchange_hospital_id(self):
        """
        This function will remove the department from the 
        department field when the hospital is changed.
        """
        self.department_id = False

    @api.onchange('hospital_id', 'department_id')
    def domain_set(self):
        """
        This function will set the domain of the department.
        """
        dept_list = []
        if self.hospital_id:
            hospital_obj = self.env['hospital.hospital'].search([('id', '=', self.hospital_id.id)])
            if hospital_obj:
                for dept in hospital_obj.department_ids:
                    dept_list.append(dept.id)
            return {'domain': {'department_id': [('id', 'in', dept_list)]}}
