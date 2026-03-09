from django.shortcuts import render


def food_add_view(request):
    return render(request, "tracker/food_entry_form.html")


def exercise_add_view(request):
    return render(request, "tracker/exercise_entry_form.html")


def weight_add_view(request):
    return render(request, "tracker/weight_log_form.html")