from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'
    _order = 'name'

    name = fields.Char(string='Name')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    born_date = fields.Date(string='Born Date')