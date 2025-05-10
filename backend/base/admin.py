# filepath: /Users/hafriaya/Development/3IIR/S6/Django/Recettes_project/backend/base/admin.py
from django.contrib import admin
from .models import Recette

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'temps_preparation', 'description')  # Fields to display in the list view
    search_fields = ('nom', 'description')  # Fields to search
    list_filter = ('temps_preparation',)  # Filters for the sidebar

admin.site.register(Recette, RecetteAdmin)