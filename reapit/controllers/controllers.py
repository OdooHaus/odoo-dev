# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
    @http.route('/reapit/reapit/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/reapit/reapit/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('reapit.listing', {
            'root': '/reapit/reapit',
            'objects': http.request.env['reapit.reapit'].search([]),
        })

    @http.route('/reapit/reapit/objects/<model("reapit.reapit"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('reapit.object', {
            'object': obj
        })