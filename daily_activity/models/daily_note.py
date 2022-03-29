from odoo import models, fields, api, _
import hashlib

class DailyNote(models.Model):
    _name = "daily.note"
    _description = "Daily Note"

    name = fields.Char(compute="_note_id_generator", string="ID", required=True)
    note_date = fields.Datetime(string="Note Date", default=fields.Datetime.now)
    feeling_rate = fields.Selection([('bad', 'Bad'), ('nrb', 'Not Really Bad'), ('n', 'Netral'), ('ge', 'Good Enough'), ('tbd', 'The Best Day of My Life')], string="Feeling Rate")
    note_content = fields.Text(string="Note Content")
    is_note_verified = fields.Boolean(string="Verified", readonly=True)
    message_for_today = fields.Char(String="Message for Today", compute="_message_for_today")

    @api.onchange('note_content')
    def _note_id_generator(self):
        for record in self:
            if record.note_content:
                record.name = hashlib.sha256(record.note_content.encode('utf-8')).hexdigest()

    @api.depends('feeling_rate')
    def _message_for_today(self):
        for record in self:
            if record.feeling_rate == 'bad':
                record.message_for_today = "You are not doing well today. Please try to do better tomorrow."
            elif record.feeling_rate == 'nrb':
                record.message_for_today = "You are doing good. tommorow is the best day of your life."
            elif record.feeling_rate == 'n':
                record.message_for_today = "You are doing good. no worries."
            elif record.feeling_rate == 'ge':
                record.message_for_today = "You are doing good. Keep it up!"
            elif record.feeling_rate == 'tbd':
                record.message_for_today = "You are doing good. yohoo! you are the best!"
            else:
                record.message_for_today = "Your happiness is not defined. Please check your note."
                
            
