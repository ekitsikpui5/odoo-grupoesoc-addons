# -*- encoding: utf-8 -*-

# Odoo, Open Source Management Solution
# Copyright (C) 2014  Grupo ESOC <www.grupoesoc.es>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from openerp.osv import fields, orm


class partner_orp_technician(orm.Model):
    """Add orp technician field to all partners."""

    _name = _inherit = "res.partner"

    _columns = {
        "orp_technician_id" : fields.many2one(
            "res.partner",
            "ORP technician",
            help=("Technician in charge of managing this partner's "
                  "occupational risk prevention")),
    }
