# Copyright (C) 2022 Akretion (<http://www.akretion.com>).
# @author Kévin Roche <kevin.roche@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def no_default_immediate_tranfer_create(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    config_parameter = env["ir.config_parameter"].search(
        [("key", "=", "stock.no_default_immediate_tranfer")]
    )
    if config_parameter and config_parameter.value != "False":
        config_parameter.write({"value": "True"})
    else:
        env["ir.config_parameter"].create(
            {
                "key": "stock.no_default_immediate_tranfer",
                "value": "True",
            }
        )
