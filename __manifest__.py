# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence': 1,
    'summary': 'Hospital Management Summary',
    'description': 'Hospital Management Description.',
    'depends': ['base', 'website', 'mail'],
    'data': [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',
        'data/department_demo.xml',

        'views/assets.xml',
        'views/hospital_menus.xml',
        'views/res_users_view.xml',
        'views/doctor_view.xml',
        'views/hospital_view.xml',
        'views/patient_view.xml',
        'views/patient_history_view.xml',
        'views/madicine_view.xml',
        'views/department_view.xml',
        'views/test_view.xml',

        'wizards/appointment_wizard_view.xml',

        'report/patient_prescription_report_view.xml',

        'views/website_appointment_form.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
