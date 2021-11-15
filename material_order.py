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


class Material_Order(models.Model):
    _name = 'material.order'
    _description = 'Order List'


    customer = fields.Char(string="Customer Name", required=True)
    contact = fields.Char(string="Customer Email", required=True)
    # supplier_name = fields.Char(string='Supplier', required=True)
    # material = fields.Char(string="Material", required=True)
    name = fields.Char(string="Order Reference", required=True, copy=False, readonly=True, default=lambda self: _('New'))
    date = fields.Datetime('Order Deadline', 
                                # required=True,
                                # states=READONLY_STATES, 
                                index=True, copy=False, default=fields.Datetime.now)
    # products = fields.One2many('materials', 'exported')
    state = fields.Selection([
        ('queue', 'Queue') ,
        ('confirm', 'Confirmed') ,
        ('done', 'Done') ,
        ('cancel', 'Cancelled')
    ], string="Status", required=True, default='queue')
    
    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['name'] = 'New'
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('material.order') or _('New')
        res = super(Material_Order, self).create(vals)
        return res

    def action_queue(self):
        print("An Order has been placed.")
        self.state = 'queue'

    def action_confirm(self):
        print("An Order is being Processed.")
        self.state = 'confirm'

    def action_done(self):
        print("An Order has Finished.")
        self.state = 'done'

    def action_cancel(self):
        print("An Order has been Cancelled.")
        self.state = 'cancel'

    