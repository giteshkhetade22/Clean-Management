# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request 

class LoginPagecontroller(http.Controller):
    @http.route(['/user_login'], type='http', auth='public',website=True)
    def website_menu(self):
        return request.render("clean.webpage_login_template")
    
    @http.route(['/user_submit'],type='http',auth="public",website=True)
    def website_submit_login(self):
        return request.render('clean.login_template')
    
    @http.route('/plans', type='http', auth='public', website=True)
    def plans(self):
        plans = request.env['clean.plans'].search([])
        return request.render('clean.plans_template', {
            'plans': plans,
        })
        
    @http.route(['/booking'], type='http', auth='public', website=True)
    def booking_page(self):
        return request.render('clean.booking_page')


