# -*- coding: utf-8 -*-
# from odoo import http


# class HpTrainingOdoo(http.Controller):
#     @http.route('/hp_training_odoo/hp_training_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hp_training_odoo/hp_training_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hp_training_odoo.listing', {
#             'root': '/hp_training_odoo/hp_training_odoo',
#             'objects': http.request.env['hp_training_odoo.hp_training_odoo'].search([]),
#         })

#     @http.route('/hp_training_odoo/hp_training_odoo/objects/<model("hp_training_odoo.hp_training_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hp_training_odoo.object', {
#             'object': obj
#         })
