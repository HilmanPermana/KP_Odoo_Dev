# -*- coding: utf-8 -*-
# from odoo import http


# class HpSelfEksplor(http.Controller):
#     @http.route('/hp_self_eksplor/hp_self_eksplor/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hp_self_eksplor/hp_self_eksplor/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hp_self_eksplor.listing', {
#             'root': '/hp_self_eksplor/hp_self_eksplor',
#             'objects': http.request.env['hp_self_eksplor.hp_self_eksplor'].search([]),
#         })

#     @http.route('/hp_self_eksplor/hp_self_eksplor/objects/<model("hp_self_eksplor.hp_self_eksplor"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hp_self_eksplor.object', {
#             'object': obj
#         })
