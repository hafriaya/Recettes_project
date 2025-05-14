from django import forms
from .models import Recette, Ingredient

class RecetteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Group ingredients by category
        categories = dict(Ingredient.CATEGORIES)
        self.ingredient_categories = {}
        for category_code, category_name in Ingredient.CATEGORIES:
            ingredients = Ingredient.objects.filter(categorie=category_code)
            if ingredients.exists():
                self.ingredient_categories[category_name] = ingredients

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            'multiple': 'multiple',  # Add the multiple attribute
            'size': '5',  # Show more options at once for better UX
        }),
    )

    class Meta:
        model = Recette
        fields = ['nom', 'temps_preparation', 'description', 'ingredients', 'instructions', 'image', 'portions']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-input border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            }),
            'instructions': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-input border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            }),
            'nom': forms.TextInput(attrs={
                'class': 'form-input border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            }),
            'temps_preparation': forms.NumberInput(attrs={
                'class': 'form-input border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            }),
            'portions': forms.NumberInput(attrs={
                'class': 'form-input border border-gray-300 rounded-md shadow-sm focus:ring-culinary-500 focus:border-culinary-500',
            }),
        }