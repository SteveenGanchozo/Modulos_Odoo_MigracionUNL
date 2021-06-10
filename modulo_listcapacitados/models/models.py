# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Asistencia(models.Model):
    _name = 'reg.listcapacitados'
    _description = ''
    
    tema= fields.Text()
    fecha = fields.Datetime('Fecha', required=False, readonly=False, select=True, default=lambda self: fields.datetime.now())
    responsable = fields.Many2many('res.partner', relation='instructor_reg', required=True)
    lista = fields.Many2many('res.partner')
    observaciones = fields.Text()
    
