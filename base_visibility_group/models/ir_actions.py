from odoo import _, api, models
from odoo.exceptions import AccessError


class IrActionsActWindow(models.Model):
    _inherit = "ir.actions.act_window"


    @api.depends('view_ids.view_mode', 'view_mode', 'view_id.type')
    def _compute_views(self):
        for act in self:
            allowed_actions = self.env['ir.actions.act_window'].search([
                ('id', 'in', self.env.user.groups_id.mapped('allowed_action_ids').ids)
            ])
            if allowed_actions and act not in allowed_actions:
                raise AccessError(
                    _("You don't have enough access rights to run this action.")
                )

        return super()._compute_views()
