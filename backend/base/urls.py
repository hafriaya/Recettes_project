from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('recettes/', views.ListeRecettes.as_view(), name='recettes'),
]
