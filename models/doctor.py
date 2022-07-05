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
    ]

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Name', compute='_get_full_name')
    doctor_code = fields.Char(string='Doctor Code', required=True, 
            copy=False, readonly=True, index=True, default=lambda self: _('New'))
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age', compute='_get_age')
    gender = fields.Selection([('male', 'Male'), 
            ('female', 'Female')], string='Gender', default='male')
    img = fields.Binary(string='Profile Image', attachment=True)
    address = fields.Text(string='Address')

    hospital_id = fields.Many2one(
        'hospital.hospital', string='Assigned Hospital')

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

