# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 eagle-erp Consulting Service Pvt.Ltd (<http://www.eagle-erp.com>).
#
#    For Module Support : eagle-erp@gmail.com  or Skype : eagle-erp
#
##############################################################################

{
    'name': 'Employee Number',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Human Resources',
    'description':
        """
        This Module add below functionality into odoo

        1.This module helps you to display unique Employee Number on Employee screen

    """,
    'summary': 'Odoo app will add Employee Number on Employee screen',
    'depends': ['hr'],
    'data': [
        'views/employee_sequence.xml',
        'views/employee_view.xml'
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    #author and support Details ==========#
    'author': 'eagle-erp Consulting Service Pvt.Ltd',
    'website': 'http://www.eagle-erp.com',    
    'maintainer': 'eagle-erp Consulting Service Pvt.Ltd', 
    'support': 'eagle-erp@gmail.com',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
