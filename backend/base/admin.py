from django.contrib import admin
from .models import Recette, Ingredient

@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'temps_preparation', 'portions', 'favorite', 'date_creation')
    list_filter = ('date_creation', 'favorite')
    search_fields = ('nom', 'description', 'ingredients__nom')
    filter_horizontal = ('ingredients',)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom',)
    ordering = ('nom',)
    list_per_page = 20

admin.site.register(Ingredient, IngredientAdmin)