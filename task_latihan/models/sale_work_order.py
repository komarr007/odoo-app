from email.policy import default
from odoo import models, fields, api

class WorkOrder(models.Model):
    _name = "sale.work.order"

    name = fields.Char(string="WO Number", required=True, readonly=True, default='new')
    sale_order_id = fields.Many2one('sale.order', string="Booking Order Ref", default=False, required=True, readonly=False)
    team_id = fields.Many2one('crm.team', string="Service Team", default=False, required=True, readonly=False)
    team_leader_id = fields.Many2one('res.users', string="Service Team Leader", default=False, required=True, readonly=False)
    team_member_ids = fields.Many2many('res.users', string="Service Members", default=False, required=True, readonly=False)
    planned_start = fields.Datetime(string="Planned Start", default=False, required=True, readonly=False)
    planned_end = fields.Datetime(string="Planned End", default=False, required=True, readonly=False)
    sale_order_id = fields.Many2one('sale.order', string="Booking Order Ref", default=False, required=True, readonly=False)
    due_date = fields.Char(compute="_due_date" ,string="Due Date", required=False, readonly=True)
    state = fields.Selection(
        [('pending', 'Pending'), ('in_progress', 'In_Progress'),
         ('done', 'Done'), ('cancel', 'Cancel')], string="Status", default='pending', readonly=True)
    notes = fields.Text(string="Notes", default=False, required=False, readonly=False)

    @api.depends('planned_start', 'planned_end')
    def _due_date(self):
        for rec in self:
            if rec.planned_start and rec.planned_end:
                days_left = rec.planned_end - rec.planned_start
                rec.due_date = str(days_left)
            else:
                rec.due_date = "try to input planned start and end"