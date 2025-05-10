from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('recettes/', views.ListeRecettes.as_view(), name='recettes'),
    path('fridge/', views.WhatsInMyFridge.as_view(), name='fridge'),
    path('search/', views.SearchRecettes.as_view(), name='search'),
    path('recettes/<int:pk>/', views.RecetteDetailView.as_view(), name='recette_detail'),
]
