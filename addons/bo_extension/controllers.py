# -*- coding: utf-8 -*-
from openerp import http

# class BoExtension(http.Controller):
#     @http.route('/bo_extension/bo_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bo_extension/bo_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bo_extension.listing', {
#             'root': '/bo_extension/bo_extension',
#             'objects': http.request.env['bo_extension.bo_extension'].search([]),
#         })

#     @http.route('/bo_extension/bo_extension/objects/<model("bo_extension.bo_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bo_extension.object', {
#             'object': obj
#         })