# -*- coding: utf-8 -*-
{
    'name': "daily activity",

    'summary': """your note for increasing your life value""",

    'description': """
        I hope you remember this note as an your progress note.
        you need this note to increase your life value.
        hope you will remember this note.
    """,

    'author': "your another self",
    'website': "komarr007.github.io/RIGAQI",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/note_page_views.xml',
        'views/daily_checker_views.xml',
        'views/yt_video_download_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
