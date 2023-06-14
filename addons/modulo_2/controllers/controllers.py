# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo2(http.Controller):
#     @http.route('/modulo_2/modulo_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_2/modulo_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_2.listing', {
#             'root': '/modulo_2/modulo_2',
#             'objects': http.request.env['modulo_2.modulo_2'].search([]),
#         })

#     @http.route('/modulo_2/modulo_2/objects/<model("modulo_2.modulo_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_2.object', {
#             'object': obj
#         })
