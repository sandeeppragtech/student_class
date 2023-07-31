# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class SportsAcademy(models.Model):
    _name = 'sports.academy'
    _description = 'SportsAcademy'

    def _default_validity_date(self):    	
        # if self.env['ir.config_parameter'].sudo().get_param('sale.use_quotation_validity_days'):        	
        days = 3       
        print("q"*88,datetime.now() ) 	
        if days > 0:            	
            return fields.Date.to_string(datetime.now() + timedelta(days))   	
        return False

    name = fields.Char()
    value = fields.Integer()
    state = fields.Selection([('draft', 'Quotation'),('sent', 'Quotation Sent'),('sale', 'Sales  Order'),('done', 'Locked'),('cancel', 'Canceled')], string='Status', default='draft')
    user_id = fields.Many2one('res.users', string='Salesperson',default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', string='Company',
        default=lambda self: self.env.company)
    validity_date = fields.Datetime(string='Expiration',states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},default=_default_validity_date)
    company_email = fields.Char(string="Company Email")
    is_number =  fields.Boolean("Is Number")
    description =  fields.Text("Description")
    partner_ids = fields.Many2many('res.partner','partner_academy_rel','partner_id','academy_id')

    def default_get(self, fields_list):
        res = super(SportsAcademy, self).default_get(fields_list)
        res.update({'company_email': self.env.company.email})
        return res

    # def _default_validity_date(self):    	
    #     # if self.env['ir.config_parameter'].sudo().get_param('sale.use_quotation_validity_days'):        	
    #     days = 3        	
    #     if days > 0:            	
    #         return fields.Date.to_string(datetime.now() + timedelta(days))   	
    #     return False
