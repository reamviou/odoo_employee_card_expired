# -*- coding: utf-8 -*-
###############################################################################

###############################################################################
{
    'name': 'Employee Card Expired Date',
    'version': '18.0.1.0.1',
    'category': 'HR',
    'summary': """Employee Card expired date, Odoo card expired date""",
    'author': "V Technologies",
    'company': 'V Technologies',
    'maintainer': 'V Technologies',
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
