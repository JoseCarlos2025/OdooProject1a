from odoo import models, fields, api

class Proyecto1a_EmpresaContratadora(models.Model):
    _name = 'proyecto1a.empresa_contratadora'
    _description = 'Empresas Contratadoras'

    name = fields.Char(string='Nombre empresa contratadora', required=True)
    correo_empresa_contratadora = fields.Char(string='Email empresa contratadora', required=True)
    proyectos = fields.One2many('project.project', 'empresa_contratadora', string='Proyectos Contratados', ondelete='cascade')

    proyectos_contratados_count = fields.Integer(string='Proyectos Contratados', compute='_proyectos_contratados_cuenta', store=True)

    @api.depends('proyectos')
    def _proyectos_contratados_cuenta(self):
        for empresa_contratadora in self:
            empresa_contratadora.proyectos_contratados_count = len(empresa_contratadora.proyectos)


class Proyecto1a_Proyecto(models.Model):
    _name = 'project.project'
    _inherit = 'project.project'

    empresa_contratadora = fields.Many2one('proyecto1a.empresa_contratadora', ondelete='cascade')
    tareas = fields.One2many('project.task', 'proyecto', string='Proyectos Contratados', ondelete='cascade')

class Proyecto1a_Tarea(models.Model):
    _name = 'project.task'
    _inherit = 'project.task'

    proyecto = fields.Many2one('project.project', string='Proyectos', ondelete='cascade')
    subtareas = fields.One2many('project.task', 'tarea_padre', string='Subtareas', ondelete='cascade')
    tarea_padre = fields.Many2one('project.task', string='Tarea Padre', ondelete='cascade')

    @api.model
    def filtro_tareas_sin_tarea_padre(self):
        return [('tarea_padre', '=', False)]



