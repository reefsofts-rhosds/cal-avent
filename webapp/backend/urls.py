#urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('eleve-au-hasard/', views.eleve_au_hasard, name='eleve-au-hasard'),
    path('combien/', views.cmb_eleves_aujourdhui, name="cmb-eleves-aujourdhui"),
    path('', views.rootpage, name='rootpage'),
]