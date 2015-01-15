# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class promociones(osv.Model):

	_name = 'cybex.promociones'
	_columns = {
	    'flag':fields.boolean('Activa',help="indica si es una promocion vigente"),
	    'name': fields.char('Nombre', help="Ingrese un nombre ",required="1"),
	    'description':fields.char('Descripcion',help="Ingrese una descripcion",required="1"),
            'tiempo': fields.integer('Dias Gratis', help="la cantidad de meses gratis", required="1"),
}

	

	_defaults={

		'flag':True

}


class promo_contrato(osv.Model):
    _name = "promocontrato"
    _rec_name = 'promo'
    _columns = {
        'promo': fields.many2one('cybex.promociones', string="Promociones"),
        'contrato_id': fields.many2one('sale.recurring_orders.agreement', string="Contratos"),
            }
