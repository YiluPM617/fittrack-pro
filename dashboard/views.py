from django.shortcuts import render


def dashboard_view(request):
    context = {
        "calories_in": 1800,
        "calories_out": 450,
        "net_calories": 1350,
        "current_weight": 72.5,
    }
    return render(request, "dashboard/dashboard.html", context)
