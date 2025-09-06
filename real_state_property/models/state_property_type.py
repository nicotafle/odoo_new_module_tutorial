from odoo import fields, models

class StatePropertyType(models.Model):
    _name = "state.property.type"
    _description = "State Property Type"

    name = fields.Char(string= "Type of property")