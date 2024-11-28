from django.contrib import admin
from .models import Eleve
from unfold.admin import ModelAdmin

class EleveAdmin(ModelAdmin):
    list_display = ('nom', 'prenom', 'utilise', 'numero_ordre_alphabetique', 'boite')
    actions = ['remettre_a_zero']

    def remettre_a_zero(self, request, queryset):
        queryset.update(utilise=False)
    remettre_a_zero.short_description = "Remettre à zéro le champ qui définit l'accès à une boite des eleves selectionnés."
admin.site.register(Eleve, EleveAdmin)
