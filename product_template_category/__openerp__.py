# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2015 Goran Sunjka (http://www.sunjka.de) All Rights Reserved.
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name' : 'Product Template Category',
    'version' : '0.1',
    "author": "Goran Sunjka",
    "website": "http://www.sunjka.de",
    "license" : "AGPL-3",
    "category" : "Generic Modules/Inventory Control",
    "description": """
This module will add categories to the product template view.
    """,
    'depends' : [
        'product', 
        'product_m2mcategories', 
    ],
    "data" : [
        'product_template_category_view.xml',
    ],
    'installable': True,
    'active': False,
}
