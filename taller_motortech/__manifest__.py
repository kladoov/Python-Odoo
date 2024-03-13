# -*- coding: utf-8 -*-
{
    'name': "taller_motortech",
    'summary': """
        Taller MotorTech
        """,

    'description': """
        En mi taller, te sumergirás en un ambiente dinámico y colaborativo donde podrás explorar 
        nuevas habilidades, desatar tu creatividad y alcanzar tus metas. Con actividades 
        prácticas y orientación experta, te ayudaré a desarrollar todo tu potencial. 
        ¡Únete y convierte tus ideas en realidad!
    """,

    'author': "Aleksandr Kladov",
    'website': "http://github.com/kladoov",
    'category': 'Uncategorized',
    'version': '0.1',
    'application': 'true',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'reports/report_vehiculo.xml',
        'reports/report_ordentrabajo.xml',
        'demo/demo.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
