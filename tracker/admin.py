from django.contrib import admin
from .models import FoodEntry, ExerciseEntry, WeightLog


admin.site.register(FoodEntry)
admin.site.register(ExerciseEntry)
admin.site.register(WeightLog)