from django.db import models

class Ingredient(models.Model):
    CATEGORIES = [
        ('legumes', 'Légumes'),
        ('viandes', 'Viandes et Volailles'),
        ('produits_laitiers', 'Produits Laitiers et Œufs'),
        ('epicerie', 'Épicerie'),
        ('fruits', 'Fruits'),
        ('herbes', 'Herbes et Épices'),
    ]
    
    nom = models.CharField(max_length=100, unique=True)
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    
    class Meta:
        ordering = ['nom']
        verbose_name = 'Ingrédient'
        verbose_name_plural = 'Ingrédients'
    
    def __str__(self):
        return self.nom

class Recette(models.Model):
    nom = models.CharField(max_length=255, verbose_name='Nom de la recette')
    temps_preparation = models.IntegerField(verbose_name='Temps de préparation (minutes)')
    description = models.TextField(verbose_name='Description')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='Ingrédients')
    instructions = models.TextField(verbose_name='Instructions', blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['nom']
        verbose_name = 'Recette'
        verbose_name_plural = 'Recettes'
    
    def get_ingredients_list(self):
        return [ing.nom.lower() for ing in self.ingredients.all()]
    
    def __str__(self):
        return self.nom