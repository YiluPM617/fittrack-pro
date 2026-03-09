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
        widgets = {
            "food_name": forms.TextInput(attrs={"class": "form-control"}),
            "calories": forms.NumberInput(attrs={"class": "form-control"}),
            "protein_g": forms.NumberInput(attrs={"class": "form-control"}),
            "carbs_g": forms.NumberInput(attrs={"class": "form-control"}),
            "fat_g": forms.NumberInput(attrs={"class": "form-control"}),
            "meal_type": forms.Select(attrs={"class": "form-select"}),
        }


class ExerciseEntryForm(forms.ModelForm):
    class Meta:
        model = ExerciseEntry
        fields = [
            "exercise_name",
            "duration_minutes",
            "calories_burned",
        ]
        widgets = {
            "exercise_name": forms.TextInput(attrs={"class": "form-control"}),
            "duration_minutes": forms.NumberInput(attrs={"class": "form-control"}),
            "calories_burned": forms.NumberInput(attrs={"class": "form-control"}),
        }


class WeightLogForm(forms.ModelForm):
    class Meta:
        model = WeightLog
        fields = [
            "weight_kg",
        ]
        widgets = {
            "weight_kg": forms.NumberInput(attrs={"class": "form-control"}),
        }