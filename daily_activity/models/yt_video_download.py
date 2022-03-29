from odoo import models, fields, api, _
from pytube import YouTube

class YtVideoDownload(models.Model):
    _name = "yt.video.download"
    _description = "Youtube Video Download"

    name = fields.Char(string="Video Topic", required=True)
    video_url = fields.Char(string="Video URL", required=True)
    resolution = fields.Char(string="Resolution", required=True)
    video_format = fields.Char(string="Video Format", required=True)
    outpath = fields.Char(string="Output Path", required=True)

    def video_download(self):
        for record in self:
            yt = YouTube(record['video_url'])
            stream = yt.streams.filter(file_extension=record['video_format'])
            stream_final = stream.get_by_resolution(record['resolution'])
            stream_final.download(filename=record['name']+"."+record['video_format'], output_path=record['outpath'])


    