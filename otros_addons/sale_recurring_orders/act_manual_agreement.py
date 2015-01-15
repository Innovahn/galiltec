# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
from openerp.tools.translate import _
import datetime
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

class act_manual_agreement(osv.Model):

	_name = 'cybex.act_manual_agreement'
	_columns = {
	    'name': fields.char('Descripcion', help="Descripcion",required="1"),
            'tipo' : fields.selection([('a','Activar'),
                                    ('d','Desactivar')], string="Tipo",required="1"),
	    'fecha': fields.date('Fecha Actual', help="fecha", required="1"),
	    'agreement_id':fields.many2one('sale.recurring_orders.agreement',string="clientes",help="cliente"),
}

	def create(self, cr, uid, values, context=None):
		flag=False
		sale_obj=self.pool.get('sale.order')
		active_obj=self.pool.get('cybex.active')
		b =super(act_manual_agreement, self).create(cr, uid, values, context=context)	
		linea = self.browse(cr, uid, b, context=context)
		sale_ids=self.pool.get('sale.order').search(cr,uid,[('partner_id','=',linea.agreement_id.partner_id.id)])
		contador=0
		for sale in sale_obj.browse(cr,uid,sale_ids,context=context):
			if sale.state=="manual":
				
				contador+=1
		if contador>=1:
			raise osv.except_osv(_('El Grupo Tiene Pagos Pendientes'),
                    _('favor verifique los Pagos para reactivar las personas del grupo.'))
		
		if linea.tipo=='a':
			for agl in linea.agreement_id.agreement_line:
				if agl.cliente_linea_agreement.estado!=False:
					raise osv.except_osv(_('hay uno o mas miembros que estan activos'),
                   			_('favor verifique los datos de los clientes y activelos de manera individual.'))
				
			for agl in linea.agreement_id.agreement_line:
				self.pool.get('sale.recurring_orders.agreement.line').write(cr, uid,agl.id, {'active_chk':True}, context=context)			
				self.pool.get('res.partner').write(cr, uid,agl.cliente_linea_agreement.id, {'estado':True}, context=context)
				active_obj.create(cr, uid,{'name':'Activado','fecha_ad':datetime.today(),'socio_id':agl.cliente_linea_agreement.id,'descripcion':linea.name,'tipo':'Contrato','usuario':uid},context=context)	
				
		if linea.tipo=='d':
			for agl in linea.agreement_id.agreement_line:
				if agl.cliente_linea_agreement.estado!=True:
					raise osv.except_osv(_('hay uno o mas miembros que estan Desactivados'),
                   			_('favor verifique los datos de los clientes y activelos de manera individual.'))
				
			for agl in linea.agreement_id.agreement_line:
				self.pool.get('sale.recurring_orders.agreement.line').write(cr, uid,agl.id, {'active_chk':False}, context=context)			
				self.pool.get('res.partner').write(cr, uid,agl.cliente_linea_agreement.id, {'estado':False}, context=context)
				active_obj.create(cr, uid,{'name':'Desactivado','fecha_ad':datetime.today(),'socio_id':agl.cliente_linea_agreement.id,'descripcion':linea.name,'tipo':'Contrato','usuario':uid},context=context)




		return b


