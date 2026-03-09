from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodEntryForm, ExerciseEntryForm, WeightLogForm


@login_required
def food_add_view(request):
    if request.method == "POST":
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.save()
            return redirect("dashboard:home")
    else:
        form = FoodEntryForm()

    return render(request, "tracker/food_entry_form.html", {"form": form})


@login_required
def exercise_add_view(request):
    if request.method == "POST":
        form = ExerciseEntryForm(request.POST)
        if form.is_valid():
            exercise_entry = form.save(commit=False)
            exercise_entry.user = request.user
            exercise_entry.save()
            return redirect("dashboard:home")
    else:
        form = ExerciseEntryForm()

    return render(request, "tracker/exercise_entry_form.html", {"form": form})


@login_required
def weight_add_view(request):
    if request.method == "POST":
        form = WeightLogForm(request.POST)
        if form.is_valid():
            weight_log = form.save(commit=False)
            weight_log.user = request.user
            weight_log.save()
            return redirect("dashboard:home")
    else:
        form = WeightLogForm()

    return render(request, "tracker/weight_log_form.html", {"form": form})