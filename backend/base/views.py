from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .ressources.recettes import recettes
from .models import Recette 
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'hello.html',{})
class ListeRecettes(View):
    def get(self, request):
        recettes = Recette.objects.all()  # Fetch all Recette objects from the database
        return render(request, 'listeRecettes.html', {'recettes': recettes})