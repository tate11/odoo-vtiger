# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    vtiger_id = fields.Char('VTiger ID', readonly=True)
