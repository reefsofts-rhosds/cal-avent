import random
from django.db import models

groupesAP=[
    ('MA', "Groupe 1: Mardi"),
    ("JE", "Groupe 2: Jeudi"),
]

def generate_unique_id():
    while True:
        random_id = random.randint(1, 32)
        if not Eleve.objects.filter(boite=random_id).exists():
            return random_id

class Eleve(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    groupe_AP = models.CharField(max_length=2, choices=groupesAP)
    utilise = models.BooleanField()
    numero_ordre_alphabetique = models.IntegerField()
    boite = models.IntegerField(default=generate_unique_id, editable=False, unique=True)
