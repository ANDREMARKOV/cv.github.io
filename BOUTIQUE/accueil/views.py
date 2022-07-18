from django.http import HttpResponse
from django.shortcuts import render

def accueil_view(request):
    return render(request, 'accueil/accueil.html')