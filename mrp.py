# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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

from openerp import models, fields, api, _
#import time

class mrp_production(models.Model):
	_inherit = 'mrp.production'

	@api.multi
	def _get_workcenter(self):
		value = 'N/D'
		if not self.bom_id:
			return value
		else:
			if not self.bom_id.routing_id:
				return value
			else:
				value = self.bom_id.routing_id.name
				print 'CENTRO DE PRODUCCION: ', self.bom_id.routing_id.name
				return value


	@api.multi
	def _get_lot_number(self):
		value = 'N/D'
		if not self.move_finished_ids:
			return value
		else:
			if not self.move_finished_ids[0].quant_ids:
				return value
			else:
				value = self.move_finished_ids[0].quant_ids[0].lot_id.name
				return value


	def _get_current_user(self):
		return self.user_id.name

	@api.one
	def _get_kilos(self, line):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			value = self.move_raw_ids[line].kilos
			return value
			
	@api.one
	def _get_percentage(self,line):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			value = self.move_raw_ids[line].porcentaje
			return value

	@api.one
	def _get_production_ldm_quantity(self,line):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			value = self.move_raw_ids[line].product_uom_qty
			return value

	@api.multi
	def _get_total_ldm_quantity(self):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			for rec in self.move_raw_ids:
				value += rec.product_uom_qty
			return value

	@api.multi
	def _get_total_percentage(self):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			for rec in self.move_raw_ids:
				value += rec.porcentaje
			return value

	@api.multi
	def _get_total_kilos(self):
		value = 0.0
		if not self.move_raw_ids:
			return value
		else:
			for rec in self.move_raw_ids:
				value += rec.kilos
			return value