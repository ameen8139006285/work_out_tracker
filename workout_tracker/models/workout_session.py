from odoo import models, fields

class WorkoutSession(models.Model):
    _name = "workout.session"
    _description = "Workout Session"
    _rec_name = "date"

    date = fields.Date(string="Date", required=True, default=fields.Date.today)
    day = fields.Selection(
        [
            ("monday", "Monday"),
            ("tuesday", "Tuesday"),
            ("wednesday", "Wednesday"),
            ("thursday", "Thursday"),
            ("friday", "Friday"),
            ("saturday", "Saturday"),
            ("sunday", "Sunday"),
        ],
        string="Day",
        required=True
    )
    state = fields.Selection([
    ('draft', 'Draft'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed')
    ], string="Status", default='draft', tracking=True)
    trainer_id = fields.Many2one("res.users", string="Trainer")
    notes = fields.Text(string="Notes")
    attachment_ids = fields.Many2many("ir.attachment", string="Attachments")
    workout_type_id = fields.Many2one(
        "workout.type", string="Workout Type", required=True
    )
    exercise_ids = fields.One2many("workout.exercise", "session_id", string=" ")

    def action_start_workout(self):
        self.state = 'ongoing'
    
    def action_complete_workout(self):
        self.state = 'completed'