from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPassenger(models.Model):
    _name = 'res.passenger'
    _description = 'Passenger'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Name', tracking=True)
    gender = fields.Selection([("laki-laki","Laki-Laki"),("perempuan","Perempuan")], string='Gender')
    weight = fields.Float(string='Weight(Kg)')
    height = fields.Float(string='Height(Cm)')
    born_date = fields.Date(string='Born Date')