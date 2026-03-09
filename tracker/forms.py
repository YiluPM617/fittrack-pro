from django import forms
from .models import FoodEntry, ExerciseEntry, WeightLog


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = [
            "food_name",
            "calories",
            "protein_g",
            "carbs_g",
            "fat_g",
            "meal_type",
        ]


class ExerciseEntryForm(forms.ModelForm):
    class Meta:
        model = ExerciseEntry
        fields = [
            "exercise_name",
            "duration_minutes",
            "calories_burned",
        ]


class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = [
            "weight_kg",
        ]