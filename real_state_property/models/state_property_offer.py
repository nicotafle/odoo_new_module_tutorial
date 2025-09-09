from odoo import fields, models, api

class StatePropertyOffer(models.Model):
    _name = 'state.property.offer'
    _description = 'State Property Offer'

    price = fields.Float(string= 'Offer Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], copy= False)
    partner_ids = fields.Many2one(comodel_name='res.partner', string= 'Partner', required= True)
    property_ids = fields.Many2one(comodel_name='state.property', required= True)
    validity = fields.Integer(string= 'Validity (days)', default= 7)
    date_deadline = fields.Date(string= 'Date Deadline', compute= '_compute_date_deadline')

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.add(record.create_date or fields.Date.today(), days= record.validity)

    def action_confirm(self):
        for record in self:
            if record.property_ids:
                record.property_ids.write({
                    'state':'sold',
                    'partner_ids': record.partner_ids,
                    'selling_price': record.price,
                })
                record.status = 'accepted'
    
    def action_cancel(self):
        for record in self:
            record.status = 'canceled'