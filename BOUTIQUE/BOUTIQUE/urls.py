from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from clients.views import connexion_view, deconnexion_view, redirect_view, inscription_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),
    path('articles/', include('articles.urls')),
    path('connexion/', connexion_view, name='connexion'),
    path('deconnexion/', deconnexion_view, name='deconnexion'),
    path('redirect/',  redirect_view, name='redirect'),
    path('inscription/', inscription_view, name='inscription'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)