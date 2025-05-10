from django.contrib import admin
from .models import Ingredient, Recette

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom',)
    ordering = ('nom',)
    list_per_page = 20

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'temps_preparation', 'date_creation')
    list_filter = ('date_creation',)
    search_fields = ('nom', 'description', 'ingredients__nom')
    filter_horizontal = ('ingredients',)
    readonly_fields = ('date_creation', 'date_modification')
    fieldsets = (
        ('Information de base', {
            'fields': ('nom', 'temps_preparation', 'description', 'image')  # Added 'image'
        }),
        ('Ingrédients', {
            'fields': ('ingredients',)
        }),
        ('Instructions', {
            'fields': ('instructions',)
        }),
        ('Dates', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',)
        }),
    )
    list_per_page = 20

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recette, RecetteAdmin)