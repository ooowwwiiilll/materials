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


class Suppliers(models.Model):
    _name = 'suppliers'
    _description = 'Supplier List'


    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    prod_image = fields.Image(string="Image")
    products = fields.One2many('materials', 'supplier_name')