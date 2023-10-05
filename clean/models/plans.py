from odoo import models, fields, api,_  

class Plans(models.Model):
    _name = 'clean.plans'
    _description = 'Plans Information'
    
    name = fields.Char(string="Name")
    image = fields.Binary(string='Image')