# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vtiger_id = fields.Char('VTiger ID', readonly=True)
