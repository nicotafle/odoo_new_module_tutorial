from odoo import fields, models

class StatePropertyTag(models.Model):
    _name = 'state.property.tag'
    _description = 'State Property Tag'

    name =  fields.Char(string= 'Name', required= True)
    