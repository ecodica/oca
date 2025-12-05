from odoo import api, models, tools


class IrUiMenu(models.Model):
    _inherit = "ir.ui.menu"

    @api.model
    @tools.ormcache("frozenset(self.env.user.groups_id.ids)", "debug")
    def _visible_menu_ids(self, debug=False):
        """Return the ids of the menu items visible to the user."""
        visible = super()._visible_menu_ids(debug=debug)
        context = {"ir.ui.menu.full_list": True}
        menus = self.with_context(**context).browse(visible)
        groups = self.env.user.groups_id
        allowed_menus = groups.mapped('allowed_menu_ids')

        visible = menus
        if allowed_menus:
            visible = menus & allowed_menus

        return set(visible.ids)
