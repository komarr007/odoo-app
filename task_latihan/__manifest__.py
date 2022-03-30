# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Booking Order Your Name',
    'version': '1.0',
    'category': 'Sales',
    'description': """booking order""",
    'depends': [
        'base',
        'sale',
    ],
    'data': [
      'security/ir.model.access.csv',
      'views/menu_views.xml',
      'views/service_team_views.xml',
      'views/booking_order_views.xml',
      'views/sale_work_order_views.xml',
    ],
    'demo': [
      
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}
