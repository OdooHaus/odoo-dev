# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reapit(models.Model):
    _name = 'reapit.reapit'

    name = fields.Char()
    api_id = fields.Integer()
    api_key = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.api_key = self.api_id