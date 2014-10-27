# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class bo_extension(osv.osv):
    _inherit = 'res.partner'

    _columns = { 
        'nit' : fields.char('NIT', required=False),
        'ci' : fields.char('CI', required=False),
    }
