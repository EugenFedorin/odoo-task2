# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'HR hospital',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'summary': """Hr hospital my test module """,
    'license': 'LGPL-3',
    'author': 'Eugen Fedorin',
    'website': '',
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/hospital_menus.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_visit_views.xml',

    ],
    'demo': [

        'data/hospital_disease_data.xml',
        'data/hospital_doctor_demo.xml',
        'data/hospital_patient_demo.xml',
    ],
    'support': 'egen.fedorin@gmail.com',
    'application': False,
    'installable': True,
    'auto_install': False,
}
