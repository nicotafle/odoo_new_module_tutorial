from odoo import fields, models

class StatePropertyOffer(models.Model):
    _name = 'state.property.offer'
    _description = 'State Property Offer'

    price = fields.Float(string= 'Offer Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], copy= False)
    partner_ids = fields.Many2one('res.partner', string= 'Partner', required= True)
    property_ids = fields.Many2one('state.property', required= True)
