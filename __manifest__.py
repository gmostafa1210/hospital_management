# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0',
    'sequence': 1,
    'summary': 'Hospital Management Summary',
    'description': 'Hospital Management Description.',
    'depends': ['base', 'website'],
    'data': [
        'security/hospital_security.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/hospital_menus.xml',
        'views/doctor_view.xml',
        'views/hospital_view.xml',
        'views/patient_view.xml',
        'views/patient_history.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
