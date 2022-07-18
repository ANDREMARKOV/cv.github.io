from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_view, name='articles'),
    path('panier/', views.panier_view, name="panier"),
    path('panier_vide/', views.panier_vide, name="panier_vide"),
    path('delete_panier/', views.delete_panier_view, name="delete_panier"),
    path('<slug:slug>/', views.details_view, name='details'),
    path('<slug:slug>/ajouter/', views.ajouter_view, name="ajouter"),
]
