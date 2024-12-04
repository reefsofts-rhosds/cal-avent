#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('eleve-au-hasard/', views.eleve_au_hasard, name='Eleve au hasard'),
    path('combien/', views.cmb_eleves_aujourdhui, name="Combien d'élèves aujourd'hui"),
    path('', views.rootpage, name='rootpage'),
    path('ap/mardi/au_hasard/', views.eleve_au_hasard_apm, name="Eleve (groupe d'ap 1) au hasard"),
    path('ap/jeudi/au_hasard/', views.eleve_au_hasard_apj, name="Eleve (groupe d'ap 2) au hasard"),
]