# -*- coding: utf-8 -*-
{
    'name': "bo_extension",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Alejandro Perez - Swissbytes",
    'website': "http://www.siwssbyes.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bolivian partner extension',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
         'bo_partner_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
        #'demo.xml',
    # ],
}