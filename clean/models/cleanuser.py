from odoo import models, fields, api,_


class Userclean(models.Model):
    _name = 'clean.cleanuser'
    _description = 'User Information'

    name = fields.Char(string='Name')
    age = fields.Char(string="Age")
    gender = fields.Selection([
        ('male','Male'),
        ('female', 'Female')], string= "Gender", default ='male')
    registration_number = fields.Char(string="Registration Number" , copy=False, readonly=True, default=lambda self: _('New'))
    registration_date = fields.Date(string="Registration Date")
    mobile_number = fields.Char(string="Mobile No")
    address = fields.Text(string="Address")
    
    
    @api.model
    def create(self, vals):
        if vals.get('registration_number', _('New')) == _('New'):
            vals['registration_number'] = self.env['ir.sequence'].next_by_code('clean.cleanuser') or _('New')
        return super(Userclean, self).create(vals)

    
