from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('food/add/', views.food_add_view, name='food_add'),
    path('exercise/add/', views.exercise_add_view, name='exercise_add'),
    path('weight/add/', views.weight_add_view, name='weight_add'),
]