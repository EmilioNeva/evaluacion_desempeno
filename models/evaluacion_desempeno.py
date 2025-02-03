from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación del empleado'
    
    nombre = fields.Char('Nombre del empleado', required=True)
    titulo = fields.Char('Titulo de la evaluación')
    fecha = fields.Date('Fecha de la evaluación', required=True)
    comentarios = fields.Text('Comentarios del evaluador')
    
    puntuacion = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ], string="Puntuación", default="1")
    
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('finalizada', 'Finalizada')
    ], string="Estado", default="pendiente")