from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Recette, Ingredient
from django.db.models import Q
from django.views.generic import DetailView
from django.http import JsonResponse

class Home(View):
    def get(self, request):
        return render(request, 'hello.html')

class ListeRecettes(View):
    def get(self, request):
        recettes = Recette.objects.prefetch_related('ingredients').all()
        return render(request, 'listeRecettes.html', {'recettes': recettes})

class WhatsInMyFridge(View):
    def get(self, request):
        categories = dict(Ingredient.CATEGORIES)
        ingredients_by_category = {}
        
        for category_code, category_name in Ingredient.CATEGORIES:
            ingredients = Ingredient.objects.filter(
                categorie=category_code
            ).order_by('nom')
            if ingredients.exists():
                ingredients_by_category[category_name] = {
                    'icon': self.get_category_icon(category_code),
                    'ingredients': ingredients
                }
        
        return render(request, 'fridge.html', {
            'all_recipes': Recette.objects.prefetch_related('ingredients').all(),
            'ingredients_by_category': ingredients_by_category
        })
    
    def get_category_icon(self, category):
        icons = {
            'legumes': 'fas fa-carrot',
            'viandes': 'fas fa-drumstick-bite',
            'produits_laitiers': 'fas fa-cheese',
            'epicerie': 'fas fa-wheat-alt',
            'fruits': 'fas fa-apple-alt',
            'herbes': 'fas fa-leaf'
        }
        return icons.get(category, 'fas fa-question')

class SearchRecettes(View):
    def get(self, request):
        query = request.GET.get('q', '').strip()
        if not query:
            return render(request, 'search_results.html', {'recettes': [], 'query': query})
        
        recettes = Recette.objects.filter(
            Q(nom__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__nom__icontains=query)
        ).distinct().prefetch_related('ingredients')
        
        return render(request, 'search_results.html', {
            'recettes': recettes,
            'query': query
        })
    
class RecetteDetailView(DetailView):
    model = Recette
    template_name = 'recette_detail.html'
    context_object_name = 'recette'

def toggle_favorite(request, pk):
    if request.method == 'POST':
        recette = get_object_or_404(Recette, pk=pk)
        recette.favorite = not recette.favorite
        recette.save()
        return JsonResponse({'favorite': recette.favorite})
    return JsonResponse({'error': 'Invalid request'}, status=400)