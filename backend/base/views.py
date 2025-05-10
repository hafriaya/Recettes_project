from django.shortcuts import render
from django.views import View
from .models import Recette

class Home(View):
    def get(self, request):
        return render(request, 'hello.html', {})

class ListeRecettes(View):
    def get(self, request):
        recettes = Recette.objects.all()
        return render(request, 'listeRecettes.html', {'recettes': recettes})

class WhatsInMyFridge(View):
    def get(self, request):
        return render(request, 'fridge.html', {})

    def post(self, request):
        ingredients = request.POST.getlist('ingredients')
        recettes = Recette.objects.filter(
            ingredients__icontains=','.join(ingredients)
        )
        return render(request, 'fridge_results.html', {'recettes': recettes})

class SearchRecettes(View):
    def get(self, request):
        query = request.GET.get('q', '')
        recettes = Recette.objects.filter(
            nom__icontains=query
        ) | Recette.objects.filter(
            ingredients__icontains=query
        )
        return render(request, 'search_results.html', {'recettes': recettes, 'query': query})