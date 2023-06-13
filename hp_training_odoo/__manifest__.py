# -*- coding: utf-8 -*-
{
    'name': "Training Odoo (Hilman)",

    'summary': """
        Modul Manajamen Transportasi""",
    'sequence': 1,

    'description': """
       Modul Kustom Training Untuk Manajamen Transportasi
    """,

    'author': "Hilman Permana",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'hr',
        'mail'
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/data.xml',
        'data/action_server.xml',
        'views/menuItem.xml',
        'views/res_passenger_view.xml',
        'views/bus_schedule_view.xml',
        'views/res_bus_view.xml',
        'views/bus_route_view.xml',
        'views/employee_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
