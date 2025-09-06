from odoo import models, fields

class StateProperty(models.Model):
    _name = 'state.property'
    _description = 'State Property'

    name = fields.Char(string= 'Tag Name', required= True)
    description = fields.Text(string= 'Description')
    active = fields.Boolean(default= True)
    state = fields.Selection(
        selection= [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_acepted', 'Offer Acepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
    ], string= 'Status', default= 'new', required= True)
    property_type = fields.Many2one('state_property_type.name_type')
    post_code = fields.Char(string= 'Post Code')
    date_availability = fields.Date(string= 'Availability Date', default= lambda self: fields.Date.add(fields.Date.today(), months=3), copy= False)
    expected_price = fields.Float(string= 'Expected Price', required= True)
    selling_price = fields.Float(string= 'Selling Price', readonly= True, copy= False)
    bedrooms = fields.Integer(string= 'Bedrooms', default= 1)
    living_area = fields.Integer(string= 'Living Area (sqm)')
    facades = fields.Integer(string= 'Facades')
    garage = fields.Boolean(string= 'Garage')
    garden = fields.Boolean(string= 'Garden')
    garden_area = fields.Integer(string= 'Garden Area')
    garden_orientation = fields.Selection(string= 'Garden Orientation',
                                            selection=[
                                                ('north', 'North'),
                                                ('south', 'South'),
                                                ('east', 'East'),
                                                ('west', 'West')
                                            ])
    
    