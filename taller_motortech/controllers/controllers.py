# -*- coding: utf-8 -*-
# from odoo import http


# class TallerMotortech(http.Controller):
#     @http.route('/taller_motortech/taller_motortech', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taller_motortech/taller_motortech/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taller_motortech.listing', {
#             'root': '/taller_motortech/taller_motortech',
#             'objects': http.request.env['taller_motortech.taller_motortech'].search([]),
#         })

#     @http.route('/taller_motortech/taller_motortech/objects/<model("taller_motortech.taller_motortech"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taller_motortech.object', {
#             'object': obj
#         })
