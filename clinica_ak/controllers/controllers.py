# -*- coding: utf-8 -*-
# from odoo import http


# class ClinicaAk(http.Controller):
#     @http.route('/clinica_ak/clinica_ak', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinica_ak/clinica_ak/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinica_ak.listing', {
#             'root': '/clinica_ak/clinica_ak',
#             'objects': http.request.env['clinica_ak.clinica_ak'].search([]),
#         })

#     @http.route('/clinica_ak/clinica_ak/objects/<model("clinica_ak.clinica_ak"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinica_ak.object', {
#             'object': obj
#         })
