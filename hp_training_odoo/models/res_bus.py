from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResBus(models.Model):
    _name = 'res.bus'
    _description = 'Bus'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('bus_code_unique', 'unique(code)', 'Nama kode bus harus unik!!!')
    ]

    name = fields.Char(string='Name', tracking=True)
    code = fields.Char(string='Code', tracking=True)
    capacity = fields.Integer(string='Capacity')
    image = fields.Binary(string='Image')
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("ready", "Ready"),
            ("mt", "Maintenance"),
            ("depr", "Depraicated"),
        ],
        string="Status",
        default="draft",
    )