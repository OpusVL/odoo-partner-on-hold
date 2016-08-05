# -*- coding: utf-8 -*-

##############################################################################
#
# Invoice Partner On Hold
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Invoice Partner On Hold',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Block opening of invoice if the partner is on hold',
    
    'category': 'Accounting & Finance',
    
    'description': """Block opening of invoice if the partner is on hold,
""",
    'images': [
    ],
    'depends': [
        'account',
        'partner_on_hold',
    ],
    'data': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
