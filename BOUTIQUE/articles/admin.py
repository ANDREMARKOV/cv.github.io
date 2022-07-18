from django.contrib import admin

from articles.models import Articles, Commande, Panier

admin.site.register(Articles)
admin.site.register(Commande)
admin.site.register(Panier)