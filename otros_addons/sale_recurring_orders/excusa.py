# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
import datetime
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

class excusa(osv.Model):

    _name = 'excusa'



    def _obtener_clientes(self,cr,uid,id,field,args,context=None):
	print "*"*50
	print id
	nombres=[]
	unidad=''	
	res={}
	for obj_excusa in self.browse(cr,uid,id,context=context):
	    nombres=[]
	    for clientes in obj_excusa.clientes:
		
		unidad=clientes.partner_id.name
       		nombres.append(unidad)
		
	    res[obj_excusa.id]=nombres
	    print nombres
	return res

    def _obtener_codigos(self,cr,uid,id,field,args,context=None):
	codigos=[]
	unidad=''	
	res={}
	for obj_excusa in self.browse(cr,uid,id,context=context):
	    codigos=[]
	    for codigo in obj_excusa.clientes:
		print "/"*50
		
		
		unidad=codigo.partner_id.codigo_socio
       		codigos.append(unidad)
		
	    res[obj_excusa.id]=codigos
	    
	return res	

   

	


    _columns = {
	    'csocio':fields.function(_obtener_codigos,string='Codigos',type="char"),
	    'nombres_clientes':fields.function(_obtener_clientes,string='Clientes Excusados',type="char"),	
            'name':fields.char('n°',help="Numero de excusa"),
            'fecha_creacion':fields.date('Fecha de Firma',select=1,help="fecha en que firmo la excusa",required=True),
            'fecha_inicio':fields.date('Fecha Inicio',help="Fecha de inicio de Excusa",required=True),
            'fecha_final':fields.date('Fecha de Finalizacion',help="fecha de finalizacion, en caso de ser indefinida dejar en blanco"),
            'descripcion':fields.text('Razon de Excusa',help="Razon por la cual fue creada la excusa",required=True),
            'receptor':fields.many2one('res.users','Receptor',help="Persona que recibe la excusa",required=True),
            'clientes':fields.one2many('socios','contrato_id',"Clientes",help="Clientes a los cuales afecta la excusa",required=True),
            'recurrente_id': fields.many2one('sale.recurring_orders.agreement',string="numero de contrato"),
	    'observaciones':fields.text('Observaciones',help="Ingrese las observaciones que tenga sobre la Excusa"),
        }

    


