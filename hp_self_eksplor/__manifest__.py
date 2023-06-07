# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",
    'version' : '1.0',

    'summary': """
        Hospital management software""",
    'sequence': 10,

    'description': """
        This Is Modul For Eksplor Create By Odoo to Next project in KP
    """,

    'author': "Hilman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
