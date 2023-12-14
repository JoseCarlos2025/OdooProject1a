# -*- coding: utf-8 -*-
# from odoo import http


# class Proyecto1a(http.Controller):
#     @http.route('/proyecto1a/proyecto1a', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto1a/proyecto1a/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto1a.listing', {
#             'root': '/proyecto1a/proyecto1a',
#             'objects': http.request.env['proyecto1a.proyecto1a'].search([]),
#         })

#     @http.route('/proyecto1a/proyecto1a/objects/<model("proyecto1a.proyecto1a"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto1a.object', {
#             'object': obj
#         })
