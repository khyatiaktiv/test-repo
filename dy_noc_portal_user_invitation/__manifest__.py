# -*- coding: utf-8 -*-
{
    'name': 'dy NOC Portal User Invitation',
    'version': '14.0.1.0.6',
    'description': """NOC Portal User Invitation""",
    'author': 'dygytally.de, AKTIV SOFTWARE',
    'website': 'https://www.dygytally.de',
    'category': 'Dy NOC Portal',
    'depends': ['dy_NOC', 'website'],
    'license': 'AGPL-3',
    'data': [
    	'data/portal_invitation_email_template.xml', 
        'views/noc_customer_access_views.xml', 
        'views/portal_wizard_views.xml',
        'views/res_users.xml',
        'security/security.xml',
    ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
}
