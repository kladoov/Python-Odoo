# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class Citas(models.Model):
    _name = 'clinica_ak.citas'
    _description = 'Citas'
    
    descripcion = fields.Char(string='Descripcion corta')
    fecha = fields.Date(string='Fecha')
    paciente = fields.Many2one('clinica_ak.pacientes', string='Paciente')
    
    # onChange > 10 descripcion
    @api.onchange('descripcion')
    def _warning_descripcion(self):
        if self.descripcion and len(self.descripcion) > 10:
            return {
                'warning': {
                    'title': "Valor incorrecto",
                    'message': "La descripción no puede ser superior a 10 caracteres.",
                },
            }
    
    # restriccion > 10 descripcion
    @api.constrains('descripcion')
    def _restric_descripcion(self):
        for record in self:
            if len(record.descripcion) > 10:
                raise ValidationError("La descripcion no puede ser superior a 10 caracteres.")
            
            
            

class Pacientes(models.Model):
    _name = 'clinica_ak.pacientes'
    _description = 'Pacientes'
    
    nombre = fields.Char(string='Nombre del paciente', required=True, unique=True)
    fecha_nacimiento = fields.Date(string='Fecha nacimiento')
    enfermedades = fields.Many2many('clinica_ak.enfermedades', string='Enfermedades')
    edad = fields.Integer('Edad', compute="_edadcalculado", store=True )
    numero_enfermedades = fields.Integer('Número de enfermedades', compute="_numero_enfermedades", strore=True)
    citas = fields.One2many('clinica_ak.citas', 'paciente', string='Citas')

    @api.depends('fecha_nacimiento')
    def _edadcalculado(self):
        hoy = date.today()
        for paciente in self:
            if paciente.fecha_nacimiento:
                dia = paciente.fecha_nacimiento
                año = hoy.year - dia.year - ((hoy.month, hoy.day) < (dia.month, dia.day))
                paciente.edad = año
            else:
                paciente.edad = 0
                
    @api.depends('enfermedades')
    def _numero_enfermedades(self):
        for pacientes in self:
            pacientes.numero_enfermedades = len(pacientes.enfermedades)
    
    
class Enfermedades(models.Model):
    _name = 'clinica_ak.enfermedades'
    _description = 'Enfermedades'
    
    nombre = fields.Char(string='Nombre de la enfermedad')
    pacientes = fields.Many2many('clinica_ak.pacientes', string='Pacientes')