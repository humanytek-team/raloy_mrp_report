# -*- coding: utf-8 -*-
{
    'name': 'Reportes de manufactura',
    'version': '1.1',
    'summary': 'Agrega reporte de orden dilucion y homogeneizacion',
    'category': 'Raloy',
    'description': """
    Agrega reporte de orden dilucion y homogeneizacion.
    """,
    'author': 'Humanytek',
    'website': 'http://www.humanytek.com',
    'depends': ['mrp'],
    'data': [
        'report/mrp_dilution_homogenization_order.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: