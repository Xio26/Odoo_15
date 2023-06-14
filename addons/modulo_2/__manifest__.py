# -*- coding: utf-8 -*-
{
    'name': "modulo_2",

    'summary': """
        Modulo de Cumpleaños""",

    'description': """
        Segundo modulo: Modulo para insertar cumpleaños y alertar de estos
    """,

    'author': "Xiomara Vásquez",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner_hb.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
