from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Evaluación del empleado'
    nombre = fields.Char('Nombre del empleado', required=True)
    titulo = fields.Char('Titulo de la evaluación')
    observaciones = fields.Text('Observaciones sobre el desempeno del empleado')
    fecha = fields.Date('Fecha de la evaluación', required=True)
    comentarios = fields.Text('Comentarios del evaluador')
    puntuacion = fields.Selection(
        ["1","2","3","4","5","6","7","8","9","10"],
        string = "Puntuación",
        defautl = "1"
    )
    
    estado = fields.Selection(
        [
           "Pendiente",
            "En proceso",
            "Finalizada",
        ],
        string="Estado",
        default="Pendiente"
    )
    
    
    
    
    
    @api.model
    def get_evaluacion(self):
        return self.env['evaluacion.desempeno'].search([])