# -*- coding: utf-8 -*-

from odoo import models,fields,api

class ResParnertAge(models.Model):

    _inherit = 'res.partner'
    date_of_birth = fields.Date(string=u'Fecha de cumpleaños', track_visibility='onchange')
    sex = fields.Selection([('masculino','Masculino'),('femenino','Femenino'),('ND','No Definido')], track_visibility='onchange')
    pasarporte = fields.Char(string=u'Pasaporte', default='=000-000', help='Debe de contener 8 digitos', track_visibility='onchange')
    extranjero = fields.Boolean(string='Extranjero', default=False, track_visibility='onchange')
