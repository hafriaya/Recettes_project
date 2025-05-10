from django import forms
from .models import Recette, Ingredient

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['nom', 'temps_preparation', 'description', 'ingredients', 'instructions']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nom', 'categorie']