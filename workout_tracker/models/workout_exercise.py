from odoo import models, fields,api,_

class WorkoutExercise(models.Model):
    _name = "workout.exercise"
    _description = "Workout Exercise"

    session_id = fields.Many2one("workout.session", string="Workout Session", required=True)
    item_name = fields.Many2one("workout.item.master", string="Exercise", required=True)
    set_ids = fields.One2many("workout.exercise.set", "exercise_id", string="Sets")

class WorkoutExerciseSet(models.Model):
    _name = "workout.exercise.set"
    _description = "Workout Exercise Set"

    exercise_id = fields.Many2one("workout.exercise", string="Exercise", required=True, ondelete="cascade")
    set_number = fields.Integer(string="Set Number", required=True)
    reps = fields.Integer(string="Reps", required=True)
    weight = fields.Float(string="Weight (kg)", required=True)
    display_name = fields.Char(compute="_compute_display_name", store=True)

    @api.depends("set_number", "reps", "weight")
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"Set {record.set_number}: {record.reps} reps, {record.weight} kg"