from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from itertools import groupby
from pytz import timezone, UTC
from werkzeug.urls import url_encode

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang


class Materials(models.Model):
    _name = 'materials'
    _description = 'Material List'


    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)    
    type = fields.Selection([
        ('fabric', 'Fabric') ,
        ('jeans', 'Jeans') ,
        ('cotton', 'Cotton') ,
    ], string='Type', required=True)
    price = fields.Float(string='Buy Price', required=True, default=100.000) #Price in IDR
    supplier_name = fields.Many2one('suppliers', string='Supplier', required=True)
    picture = fields.Image(string="Image")
    # exported = fields.Many2one('material.order',string="")

    # @api.model
    # def create(self, vals_list):
    #     res = super().create(vals_list)
    #     vals_list = {
    #         'name' : res.name
    #     }
    #     self.env['material.order'].create(vals_list)
    #     return res

    # def confirm_order(self):
    #     vals = {
    #         'name' : self.name
    #     }
    #     self.env['material.order'].create(vals)

    @api.constrains('price')
    def check_price(self):
        for record in self:
            if record.price < 100.000:
                raise ValidationError(("Price Cannot less than IDR 100.000."))
            else :
                True

