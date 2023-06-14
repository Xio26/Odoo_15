from odoo import models,fields

class Todo(models.Model):
    _name = "xv.todo"

    name = fields.Char("Nombre")
    status = fields.Selection(selection=[("borrador","Borrador"),("hecho","Hecho")])
    date = fields.Date()
    date_hb = fields.Date(string=u'Fecha de cumpleaños')