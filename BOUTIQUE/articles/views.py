from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Articles, Commande, Panier
from django.contrib.auth.decorators import login_required

@login_required

def articles_view(request):
    articles=Articles.objects.all()
    return render(request, "articles/mes_articles.html", context={'articles': articles})

def details_view(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    return render(request, "articles/details.html", context={'article':article})

def ajouter_view(request, slug):
    utilisateur = request.user
    article = get_object_or_404(Articles, slug=slug)
    panier, _ = Panier.objects.get_or_create(utilisateur=utilisateur)
    commande, created = Commande.objects.get_or_create(utilisateur=utilisateur, 
                                                                  ordered=False,
                                                                  article=article)
    if created:
        panier.mes_commandes.add(commande)
        panier.save()
    else:
        commande.quantity += 1
        commande.save()
    return redirect(reverse('articles:details', kwargs={"slug":slug}))

def panier_view(request):
    panier=get_object_or_404(Panier, utilisateur=request.user)
    return render(request, "articles/panier.html", context={"commandes":panier.mes_commandes.all()})

def panier_vide(request):
    return render(request, "articles/panier_vide.html")

def delete_panier_view(request):
    if panier := request.user.panier: # cart = request.user.panier
        panier.delete()

    return redirect('accueil')