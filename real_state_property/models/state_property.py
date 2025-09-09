from odoo import models, fields, api, exceptions

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
    property_type_id = fields.Many2one(comodel_name='state.property.type', string='Property Type')
    user_ids = fields.Many2one(comodel_name='res.users', string='Seller', default= lambda self: self.env.user)
    partner_ids = fields.Many2one(comodel_name='res.partner', string='Buyer', copy= False)
    tag_ids = fields.Many2many(comodel_name= 'state.property.tag', string='Property Tags')
    offer_ids = fields.One2many('state.property.offer', 'property_ids', string='Offers')
    post_code = fields.Char(string= 'Post Code')
    date_availability = fields.Date(string= 'Availability Date', default= lambda self: fields.Date.add(fields.Date.today(), months=3), copy= False)
    expected_price = fields.Float(string= 'Expected Price', required= True)
    selling_price = fields.Float(string= 'Selling Price', readonly= True, copy= False)
    bedrooms = fields.Integer(string= 'Bedrooms', default= 1)
    living_area = fields.Integer(string= 'Living Area (sqm)')
    facades = fields.Integer(string= 'Facades')
    garage = fields.Boolean(string= 'Garage')
    garden = fields.Boolean(string= 'Garden')
    garden_area = fields.Integer(string= 'Garden Area(sqm)')
    garden_orientation = fields.Selection(string= 'Garden Orientation',
                                            selection=[
                                                ('north', 'North'),
                                                ('south', 'South'),
                                                ('east', 'East'),
                                                ('west', 'West')
                                            ])
    total_area = fields.Integer(string= 'Total Area (sqm)', compute='_compute_total_area')
    best_price = fields.Integer(string='Best Offer', compute='_compute_best_price')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        """Add living area (sqm) with garden area (sqm)"""
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        """Return maximun offer"""
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default= 0)

    @api.onchange('garden')
    def _onchange_garden(self):
        """Auto-adjust fields garden area & garden orientation"""
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = None
    
    def action_sold_state(self):
        for record in self:
            if record.state == 'canceled':
                raise exceptions.UserError("Canceled properties cannot be sold")
            else:
                record.state = 'sold'
                return True
        
    def action_cancel_state(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("Sold properties cannot be cancel")
            else:
                record.state = 'canceled'
                return True


