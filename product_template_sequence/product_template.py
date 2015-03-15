# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import orm, fields
from openerp.tools.translate import _


class product_template(orm.Model):
    _inherit = 'product.template'

    _columns = {
        'template_code': fields.char('Reference',
                                    size=64,
                                    select=True,
                                    required=True),
        }

    _sql_constraints = [
        ('uniq_template_code',
         'unique(template_code)',
         'The reference must be unique'),
    ]

    _defaults = {
        'template_code': '/',
        }

    def create(self, cr, uid, vals, context=None):
        if not 'template_code' in vals or vals['template_code'] == '/':
            vals['template_code'] = self.pool.get('ir.sequence').get(
                    cr, uid, 'product.template')
        return super(product_template, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if not hasattr(ids, '__iter__'):
            ids = [ids]
        products_without_code = self.search(
                cr, uid,
                [('template_code', 'in', [False, '/']),
                 ('id', 'in', ids)],
                context=context)
        direct_write_ids = set(ids) - set(products_without_code)
        super(product_template, self).write(cr, uid,
                                           list(direct_write_ids),
                                           vals, context=context)
        for product_id in products_without_code:
            vals['template_code'] = self.pool.get('ir.sequence').get(
                    cr, uid, 'product.template')
            super(product_template, self).write(cr, uid,
                                               product_id,
                                               vals,
                                               context=context)
        return True

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        product = self.read(cr, uid, id, ['template_code'], context=context)
        if product['template_code']:
            default.update({
                'template_code': product['template_code'] + _('-copy'),
            })

        return super(product_template, self).copy(cr, uid, id, default, context)
