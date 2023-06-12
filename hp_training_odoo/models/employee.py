from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    #Tidak perlu diberi deskripsi, karena sudah ada di model hr.employee

    is_driver = fields.Boolean(string='Is Driver')

