from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Materials(models.Model):
    _name = 'materials'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)    
    type = fields.Selection([
        ('fabric', 'Fabric') ,
        ('jeans', 'Jeans') ,
        ('cotton', 'Cotton') ,
    ], string='Type', required=True)
    price = fields.Float(string='Buy Price', required=True) #Price in IDR

    @api.constrains('price')
    def check_price(self):
        for record in self:
            if record.price < 100.000:
                raise ValidationError(("Price Cannot less than IDR 100.000."))
            else :
                True

    supplier_id = fields.Many2one('suppliers', string='Supplier', required=True)

class Suppliers(models.Model):
    _name = 'suppliers'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)

class Suppliers(models.Model):
    _inherit = 'suppliers'

    supply_list = fields.One2many("materials", "supplier_id", string="Supply List")