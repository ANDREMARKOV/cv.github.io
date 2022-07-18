from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription_view, name='inscription'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
    path('redirect/', views.redirect_view, name='redirect'),
]