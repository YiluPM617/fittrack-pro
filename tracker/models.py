from django.db import models
from django.contrib.auth.models import User


class FoodEntry(models.Model):

    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    food_name = models.CharField(max_length=100)

    calories = models.IntegerField()

    protein_g = models.FloatField()

    carbs_g = models.FloatField()

    fat_g = models.FloatField()

    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)

    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} ({self.calories} kcal)"

class ExerciseEntry(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    exercise_name = models.CharField(max_length=100)

    duration_minutes = models.IntegerField()

    calories_burned = models.IntegerField()

    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.exercise_name} ({self.calories_burned} kcal)"

class WeightLog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    weight_kg = models.FloatField()

    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.weight_kg} kg"