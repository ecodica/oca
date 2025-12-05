from odoo import models, fields, _
from odoo.exceptions import ValidationError


class GroupsView(models.Model):
    _inherit = 'res.groups'

    allowed_menu_ids = fields.Many2many(
        comodel_name="ir.ui.menu",
        relation="ir_ui_menu_allowed_group_rel",
        column1="gid",
        column2="menu_id",
        string="Allowed Menus",
    )

    allowed_action_ids = fields.Many2many(
        comodel_name="ir.actions.act_window",
        relation="ir_actions_act_window_allowed_group_rel",
        column1="gid",
        column2="action_id",
        string="Allowed Actions",
    )
