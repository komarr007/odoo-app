from odoo import models, fields, api

class BookingOrder(models.Model):
    # _name = 'booking.order'
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string="Booking Order", readonly=True, default=False)
    team_id = fields.Many2one("crm.team", string="Service Team", readonly=False, default=False, attrs={"required": [('is_booking_order', '=', True)]})
    team_leader_id = fields.Many2one('res.users', string="Service Team Leader", readonly=False, attrs={"required": [('is_booking_order', '=', True)]})
    team_member_ids = fields.Many2many('res.users', string="Service Team Members", readonly=False, attrs={"required": [('is_booking_order', '=', True)]})
    booking_start = fields.Datetime(string="Booking Start", readonly=False, attrs={"required": [('is_booking_order', '=', True)]})
    booking_end = fields.Datetime(string="Booking End", readonly=False, attrs={"required": [('is_booking_order', '=', True)]})
    #transaction_ids = fields.Many2many("sale.order.template", "booking_transaction_rel", "booking_id", "transaction_id", string="Transaction")
    #tag_ids = fields.Many2many("sale.order.template", "booking_tag_rel", "booking_id", "tag_ids", string="Tag")

    # @api.onchange('team_id')
    # def onchange_team_id(self):
    #     self.team_leader_id = self.team_id.team_leader_id.id
    #     self.team_member_ids = self.team_id.team_member_ids.ids