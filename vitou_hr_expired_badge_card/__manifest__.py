# -*- coding: utf-8 -*-
###############################################################################

###############################################################################
{
    'name': 'HR Employee Expired Date',
    'version': '18.0.1.0.0',
    'category': 'HR',
    'summary': """This module add expired date in card of employee""",
    'author': "V Technologies",
    'company': 'V Technologies',
    'maintainer': 'Mr. REAM Vitou, Tel: (+855) 17 82 66 82',
    'website': 'https://apps.odoo.com/apps/modules/browse?search=vitou',
    'depends': ['hr'],
    'license': 'OPL-1',
    'data': [

        'views/vitouhr_employee_expired_on_card.xml',
        'views/vitouhr_employee_expired_on_card_badge.xml',

    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    "application": False,
}
