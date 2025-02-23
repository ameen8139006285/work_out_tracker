{
    "name": "Workout Tracker",
    "version": "17.0.1.0.0",
    "category": "Fitness",
    "summary": "Track gym workouts including exercises, sets, reps, and weights.",
    "author": "Ameen Muhammed",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/workout_session_views.xml",
        "views/workout_exercise_views.xml",
        "views/workout_type_views.xml",
        "views/workout_item_views.xml",
        "views/menus_views.xml",
    ],
    "installable": True,
    "application": True,
}
