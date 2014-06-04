#-*- coding: utf-8 -*-
from datetime import time

db.define_table('clientes',
                Field('nombre'),
                Field('apellido'),
                Field('domicilio'),
                Field('telefono','integer'),
                format='%(nombre)s %(apellido)s'
)

db.define_table('establecimientos',
                Field('nombre'),
                Field('cliente',db.clientes),
                Field('domicilio'),
                Field('localidad'),
                Field('telefono'),
                Field('rubro'),
                Field('superficie', comment='Expresado en M2'),
                format='%(nombre)s'
)

db.establecimientos.rubro.requires=IS_IN_SET(['Comercial', 'Particular', 'Industrial', 'Educacional', 'Estatal'])

db.define_table('fumigadores',
                Field('nombre'),
                Field('apellido'),
                Field('domicilio'),
                Field('telefono'),
                Field('foto'),
                format='%(nombre)s %(apellido)s'
)

db.define_table('certificados',
                Field('numero', label="Certificado número"),
                Field('establecimiento', db.establecimientos),
                Field('tratamiento'),
                Field('vectTrat'),
                Field('drogaUsada', label='Droga usada'),
                Field('venenoClase', label='Clase de veneno'),
                Field('fFumigacion','date', default=request.now, label='Fecha de fumigacion'),
                Field('hora','time', default=request.now),
                Field('fVencimiento','date',label='Fecha de vencimiento'),
                Field('fumigador',db.fumigadores),
                Field('observaciones'),
                format='%(numero)s'
)

db.certificados.tratamiento.requires=IS_IN_SET(['Aspersión', 'Humo', 'Niebla', 'Otro'], multiple=True)
db.certificados.vectTrat.requires=IS_IN_SET(['Insectos', 'Roedores', 'Voladores', 'Bacterias'], multiple=True)
db.certificados.drogaUsada.requires=IS_IN_SET(['Piretroydes', 'Bromadilone', 'Otra'])

db.define_table('cobros',
                Field('certificado',db.certificados),
                Field('importe', 'float'),
                Field('saldo','float'),
                Field('cancelado','boolean')
)
