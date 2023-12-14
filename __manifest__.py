# -*- coding: utf-8 -*-
{
    'name': "proyecto1a",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'project'],

    'application': 'True',

    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/project_example_data.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
