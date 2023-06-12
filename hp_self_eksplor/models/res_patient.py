from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPatient(models.Model):
    _name = 'res.patient'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    born_date = fields.Date(string='Born Date')