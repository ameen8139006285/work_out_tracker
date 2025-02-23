from odoo import models, fields


class WorkoutItemMaster(models.Model):
    _name = "workout.item.master"
    _description = "Exercise Master"

    name = fields.Char(string="Exercise Name", required=True)
    category = fields.Selection([
        ('strength', 'Strength Training'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('balance', 'Balance'),
    ], string="Category", required=True)
