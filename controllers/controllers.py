# -*- coding: utf-8 -*-
# from odoo import http


# class GestionStock(http.Controller):
#     @http.route('/gestion_stock/gestion_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_stock/gestion_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_stock.listing', {
#             'root': '/gestion_stock/gestion_stock',
#             'objects': http.request.env['gestion_stock.gestion_stock'].search([]),
#         })

#     @http.route('/gestion_stock/gestion_stock/objects/<model("gestion_stock.gestion_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_stock.object', {
#             'object': obj
#         })

