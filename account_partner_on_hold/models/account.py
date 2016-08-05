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

from openerp import models, fields, api
from openerp.exceptions import Warning

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one
    def invoice_validate(self):
        if self.partner_id.on_hold:
            raise Warning('{} on hold'.format(self._customer_or_supplier()))
        super(AccountInvoice, self).invoice_validate()

    def _customer_or_supplier(self):
        return 'Customer' if self.type.startswith('out') else 'Supplier'

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
