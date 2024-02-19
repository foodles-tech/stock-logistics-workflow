# Copyright 2024 Foodles (https://www.foodles.co)
# @author Pierre Verkest <pierreverkest84@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    planned_consumed_date = fields.Datetime(
        "Planned consumed date",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="This is the expected consumed/usage date of the product by the customer.",
    )

    def _prepare_procurement_values(self):
        vals = super()._prepare_procurement_values()
        vals["planned_consumed_date"] = self.planned_consumed_date
        return vals

    @api.model
    def _prepare_merge_moves_distinct_fields(self):
        distinct_fields = super()._prepare_merge_moves_distinct_fields()
        distinct_fields.append("planned_consumed_date")
        return distinct_fields
