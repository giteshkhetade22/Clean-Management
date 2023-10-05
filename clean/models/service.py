from odoo import models, fields, api,_


class ServiceUser(models.Model):
    _name = 'clean.service'
    _description = 'Service Information'

    sname = fields.Selection([
        ('quickclean','Quick Clean'),
        ('basicclean', 'Basic Clean'),
        ('deepclean','Deep Clean')],string='Service Name')
    
    service_no = fields.Char(string="Service Number" , copy=False, readonly=True, default=lambda self: _('New'))
    
    
    @api.model
    def create(self, vals):
        if vals.get('service_no', _('New')) == _('New'):
            vals['service_no'] = self.env['ir.sequence'].next_by_code('clean.service') or _('New')
        return super(ServiceUser, self).create(vals)
