from openerp.osv import fields, osv

class socios(osv.Model):
    _name = "socios"
    _rec_name = 'partner_id'
    _columns = {
        'partner_id': fields.many2one('res.partner', string="Partner"),
        'contrato_id': fields.many2one('sale.recurring_orders.agreement', string="Contratos"),
            }
