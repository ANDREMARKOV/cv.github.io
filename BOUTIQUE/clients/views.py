from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse

User = get_user_model()

def inscription_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('accueil')
    return render(request, 'comptes/inscription.html')

def connexion_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('accueil')
    return render(request, 'comptes/connexion.html')

def redirect_view(request):
    return render(request, 'comptes/reconnexion.html')
    
def deconnexion_view(request):
    logout(request)
    return redirect(reverse('redirect'))