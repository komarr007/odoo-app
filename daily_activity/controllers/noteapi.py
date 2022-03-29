# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import http
from odoo.http import request
import json

class NoteController(http.Controller):
    @http.route(['/noteapi','/noteapi/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def get_note_api(self, idnya=None,**kwargs):
        if not idnya:
            note = request.env['daily.note'].search([])
            value = []
            for n in note:
                value.append({"note_date" : n.note_date,
                            "feeling_rate" : n.feeling_rate,
                            "note_content" : n.note_content,
                            "is_note_verified" : n.is_note_verified})
            return json.dumps(value, indent=4, sort_keys=True, default=str)
        else:
            noteid = request.env['daily.note'].search([('id','=',idnya)])
            value=[]
            for n in noteid:
                value.append({"note_date" : n.note_date,
                            "feeling_rate" : n.feeling_rate,
                            "note_content" : n.note_content,
                            "is_note_verified" : n.is_note_verified})
                return json.dumps(value, indent=4, sort_keys=True, default=str)


    @http.route('/createnote',auth='user', type='json', methods=['POST'])
    def createNote(self, **kw):    
        if request.jsonrequest:    
            if kw['note_content']:
                vals={
                    'note_date' : datetime.now(),
                    'feeling_rate' : kw['feeling_rate'],
                    'note_content' : kw['note_content'],
                }
                note_baru = request.env['daily.note'].create(vals)
                args = {'success': True, 'ID':note_baru.id}
                return args
