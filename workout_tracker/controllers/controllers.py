# -*- coding: utf-8 -*-
# from odoo import http


# class WorkoutTracker(http.Controller):
#     @http.route('/workout_tracker/workout_tracker', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workout_tracker/workout_tracker/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('workout_tracker.listing', {
#             'root': '/workout_tracker/workout_tracker',
#             'objects': http.request.env['workout_tracker.workout_tracker'].search([]),
#         })

#     @http.route('/workout_tracker/workout_tracker/objects/<model("workout_tracker.workout_tracker"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workout_tracker.object', {
#             'object': obj
#         })

