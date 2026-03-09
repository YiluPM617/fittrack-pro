from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tracker.models import FoodEntry, ExerciseEntry, WeightLog
import json


@login_required
def dashboard_view(request):
    food_entries = FoodEntry.objects.filter(user=request.user).order_by("-logged_at")
    exercise_entries = ExerciseEntry.objects.filter(user=request.user).order_by("-logged_at")
    weight_logs = WeightLog.objects.filter(user=request.user).order_by("logged_at")
    latest_weight = weight_logs.last()

    calories_in = sum(entry.calories for entry in food_entries)
    calories_out = sum(entry.calories_burned for entry in exercise_entries)
    net_calories = calories_in - calories_out
    current_weight = latest_weight.weight_kg if latest_weight else 0

    weight_labels = [log.logged_at.strftime("%b %d") for log in weight_logs]
    weight_data = [log.weight_kg for log in weight_logs]

    context = {
        "calories_in": calories_in,
        "calories_out": calories_out,
        "net_calories": net_calories,
        "current_weight": current_weight,
        "weight_labels": json.dumps(weight_labels),
        "weight_data": json.dumps(weight_data),
    }

    return render(request, "dashboard/dashboard.html", context)