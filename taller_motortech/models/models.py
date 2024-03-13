from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
from odoo.exceptions import UserError

class Cliente(models.Model):
    _description = 'Cliente'
    _inherit = 'res.partner'
    
    es_mecanico = fields.Boolean(string="¿Es mecanico?")
    vehiculos_ids = fields.One2many('taller_motortech.vehiculo', 'cliente_id', string='Vehículos')
    email_cliente = fields.Char(string='Correo electronico',required=True)

class Vehiculo(models.Model):
    _name = 'taller_motortech.vehiculo'
    _description = 'Vehiculo'
    
    imagen = fields.Binary(string="Imagen del vehiculo")
    marca = fields.Char(string='Marca del vehículo')
    modelo = fields.Char(string='Modelo del vehículo')
    año = fields.Date(string='Año de importación')
    años = fields.Integer('Años', compute="_edadcalculado", store=True )
    name = fields.Char(string='Matricula',required=True)
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    taller_id = fields.Many2one('taller_motortech.taller', string='Taller')
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Esta matricula ya existe en la base de datos."),
    ]
    
    # calcula los años que tiene ese vehiculo
    @api.depends('año')
    def _edadcalculado(self):
        hoy = date.today()
        for vehiculo in self:
            if vehiculo.año:
                dia = vehiculo.año
                año = hoy.year - dia.year - ((hoy.month, hoy.day) < (dia.month, dia.day))
                vehiculo.años = año
            else:
                vehiculo.años = 0
    
    # onChange > 7 matricula
    @api.onchange('name')
    def _matricula(self):
        if self.name and len(self.name) > 7:
            return {
                'warning': {
                    'title': "Valor incorrecto",
                    'message': "La matricula no puede tener mas de 7 caracteres.",
                },
            }
    
    # restriccion > 7 descripcion
    @api.constrains('name')
    def _matriculaRest(self):
        for record in self:
            if len(record.name) > 7:
                raise ValidationError("La matricula no puede tener mas de 7 caracteres.")
            

# datos de un taller especifico
class Taller(models.Model):
    _name = 'taller_motortech.taller'
    _description = 'Taller'
    
    name = fields.Char(string='Nombre del taller',required=True)
    fecha_fundacion = fields.Date(string='Año de fundacion',required=True)
    ubicacion = fields.Char(string='Ubicación')
    capacidad_maxima = fields.Integer(string='Capacidad máxima de vehículos',required=True)
    descripcion = fields.Text(string='Descripción del taller')
    #vehiculos_ids = fields.One2many('taller_motortech.vehiculo', 'taller_id', string='Vehículos en el taller')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "Este nombre de taller ya existe en la base de datos."),
    ]
    

# servicio que se le realizara al vehiculo
class Servicio(models.Model):
    _name = 'taller_motortech.servicio'
    _description = 'Servicio'
    
    name = fields.Char(string='Nombre del servicio',required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio',required=True)
    duracion_estimada = fields.Float(string='Duración Estimada',required=True)

# orden de trabajo que se le ha implementado al vehiculo
class OrdenTrabajo(models.Model):
    _name = 'taller_motortech.ordentrabajo'
    _description = 'Orden de trabajo'
    
    fecha_ingreso = fields.Date(string='Fecha de ingreso')
    fecha_retirada = fields.Date(string='Fecha retirada del vehiculo')
    estado_orden = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado')], default='pendiente', string='Estado de la Orden',required=True)
    cliente = fields.Many2one('res.partner', string='Cliente',required=True)
    vehiculo = fields.Many2one('taller_motortech.vehiculo', string='Vehiculo',required=True)
    taller = fields.Many2one('taller_motortech.taller', string='Taller',required=True)
    servicio_realizado_ids = fields.Many2many('taller_motortech.servicio', string='Servicios Realizados')
    subtotal = fields.Float(string='Subtotal', compute='_subtotal', store=True)
    duracion_total = fields.Float(string='Duración total', compute='_subtotal', strore=True)
    
    # calcula el precio total de todos los servicios realizados
    @api.depends('servicio_realizado_ids', 'duracion_total')
    def _subtotal(self):
        for record in self:
            record.subtotal = sum(servicio.precio for servicio in record.servicio_realizado_ids)
            record.duracion_total = sum(servicio.duracion_estimada for servicio in record.servicio_realizado_ids)
            
    # enviar email
    def send_email(self):
        mail_mail = self.env['mail.mail']
        email_to = self.cliente.email_cliente
          
        subject = "Albaran"
        body = "Confirmamos que ya tiene su vehiculo listo para recoger"
        
        mail_id = mail_mail.create({
        	'email_to': email_to,
			'subject': subject,
			'body_html': '<pre>%s</pre>' % body,    
        })
        
        try:
            mail_mail.send([mail_id])
            print("El correo electrónico se ha enviado correctamente.")
        except Exception as e:
            print("Ocurrió un error al enviar el correo electrónico.")