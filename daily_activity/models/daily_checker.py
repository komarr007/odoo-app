from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class DailyChecker(models.Model):
    _name = "daily.checker"
    _description = "Daily Checker"

    checker_date = fields.Datetime(string="Checker Date", default=fields.Datetime.now)
    note_date = fields.Many2one(comodel_name="daily.note", string='Note Identifier')

    @api.model
    def create(self,vals):
        record = super(DailyChecker, self).create(vals)
        for _value in self.env['daily.note'].search([('is_note_verified','=',True)]):
            print("record note date: ",record.note_date.id)
            if _value.id == record.note_date.id:
                raise ValidationError(_('Note already checked!'))
        self.env['daily.note'].search([('id','=',record.note_date.id)]).write({'is_note_verified':True})
        return record


    def unlink(self):
        for _ in self:
            self.env['daily.note'].search([('id','=',_.note_date.id)]).write({'is_note_verified':False})
        record = super(DailyChecker, self).unlink()