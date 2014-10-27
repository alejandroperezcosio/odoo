# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class bo_extension(osv.osv):
    _inherit = 'res.partner'

    _columns = { 
        'nit' : fields.integer('NIT'),
        'ci' : fields.integer('CI'),
    }
