# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal

class NOCCustomPoral(CustomerPortal):

    @route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        values = self._prepare_portal_layout_values()
        portal_connection_id = request.env['noc.portal.connection'].sudo().search([('is_active', '=', True)])
        signup_url = ''
        if portal_connection_id:
            if portal_connection_id.web_portal_link:
                signup_url = portal_connection_id.web_portal_link
            else:
                signup_url = 'http://3.69.100.197/portal/public/index.php'
        return request.redirect(signup_url)
