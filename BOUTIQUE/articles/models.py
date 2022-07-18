# from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from BOUTIQUE.settings import AUTH_USER_MODEL

class Articles(models.Model):
    nom = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    prix = models.FloatField(default=0.0)
    slug = models.SlugField(max_length=120)
    date_publication = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='default.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.quantity})"

class Commande(models.Model):
    utilisateur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date_commande = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.article.nom} ({self.quantity})"

class Panier(models.Model):
    utilisateur = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    mes_commandes = models.ManyToManyField(Commande)

    def __str__(self):
        return self.utilisateur.username

    def delete(self, *args, **kwargs):
        for commande in self.mes_commandes.all():
            commande.ordered = True
            commande.date_commande = timezone.now()
            commande.save()
            
        self.mes_commandes.clear()
        super().delete(*args, **kwargs)