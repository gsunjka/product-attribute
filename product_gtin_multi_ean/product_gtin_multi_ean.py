# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Goran Sunjka
#    Copyright 2015 Goran Sunjka
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
from openerp.addons.product_gtin import product_gtin as addon_product

class ProductEan13(orm.Model):
    _inherit = 'product.ean13'

    def _check_ean_key(self, cr, uid, ids):
        res = False
        for ean in self.browse(cr, uid, ids):
            res = addon_product.check_ean(ean.name)
            if not res:
                return res
        return res

    _constraints = [(_check_ean_key, 'Error: Invalid ean code', ['name'])]
