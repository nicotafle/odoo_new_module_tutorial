from odoo import fields, models

class StatePropertyType(models.Model):
    _name = "state.property.type"
    _description = "State Property Type"

    name_type = fields.Text(string = "Type of property")