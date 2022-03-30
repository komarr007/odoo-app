from odoo import api,fields,models

class ServiceTeam(models.Model):
    _name="booking.serviceteam"

    name=fields.Char(string="Team Name", readonly=False, default=False, required=True)
    team_leader_id=fields.Many2one("res.users",string="Team Leader", readonly=False, default=False, required=True)
    team_member_ids=fields.Many2many("res.users",string="Team Member", readonly=False, default=False, required=False)
    