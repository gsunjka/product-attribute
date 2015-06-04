# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) Goran Sunjka (<http://www.sunjka.de>)
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
    "name": "Product GTIN EAN8 EAN13 UPC JPC Support for multiple EAN Codes",
    "version": "1.1",
    "author": "Goran Sunjka, Odoo Community Association (OCA)",
    "website": "http://www.sunjka.de",
    "category": "Warehouse",
    "depends": ["product_gtin", "product_multi_ean"],
    "description": """
Product GTIN multi EAN module
===================

Replaces the check of multiple EAN13 fields with a check for EAN13, EAN8, JPC, UPC and GTIN.
    """,
    "demo": [],
    "data": [],
    "installable": True,
}
