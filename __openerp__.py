# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Dada Priyatosh <dada-p@ya.ru>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Sweden - Accounting',
    'version': '1.0',
    'category': 'Localization/Account Charts',
    'description': """
    This is a module to manage the accounting chart for Sweden in OpenERP
    =====================================================================
    """,
    'author': 'Dada Priyatosh',
    'website': 'http://missing',
    'depends': [ 'account', 'base_iban', 'base_vat', 'account_chart' ],
    'data': [ 'account_chart_sweden.xml',
              'account_tax_code_template.xml',
              'account_chart_template.xml',
              'account_tax_template.xml',
              'account_fiscal_position_template.xml'
    ],
    'demo': [],
    'installable': 'True',
#    'images': ['images'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: