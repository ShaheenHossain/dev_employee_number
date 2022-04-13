from odoo import models, fields, api, _


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    emp_seq = fields.Char("Employee Sequence", required=True, readonly=True, copy=False, default='/')
    emp_id = fields.Char("Employee ID no.")
    credit_limit = fields.Integer("Credit Limit")
    personal_number = fields.Char("Personal Number")
    company_name  = fields.Char("Company Name")
    nid_number  = fields.Char("NID Number")
    working_area  = fields.Char("Working Area")
    orderd_by = fields.Text("Ordered By")
    status = fields.Selection([('active', 'Active'), ('deactive', 'Deactive'), ('suspend', 'Suspend'), ('blocked', 'Blocked')], default='active')


    @api.model
    def create(self, vals):
        if vals.get('emp_seq',  '/') == '/':
            vals['emp_seq'] = self.env['ir.sequence'].next_by_code(
                'hr.employee') or '/'
        return super(hr_employee, self).create(vals)
        
        
    def copy(self, default=None):
        if default is None:
            default = {}
        default['emp_seq'] = '/'
        return super(hr_employee, self).copy(default=default)
        
        
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
