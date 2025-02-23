from odoo import models, fields

class WorkoutType(models.Model):
    _name = "workout.type"
    _description = "Workout Type Master"

    name = fields.Char(string="Workout Type", required=True, unique=True)
