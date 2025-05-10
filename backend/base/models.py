# filepath: /Users/hafriaya/Development/3IIR/S6/Django/Recettes_project/backend/base/models.py
from django.db import models

class Recette(models.Model):
    nom = models.CharField(max_length=255)
    temps_preparation = models.IntegerField()
    description = models.TextField()
    ingredients = models.TextField()  # Store as a comma-separated string

    def __str__(self):
        return self.nom