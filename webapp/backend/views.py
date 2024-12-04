# views.py
from django.http import HttpResponse
from .models import Eleve
import random

def eleve_au_hasard(request):
    eleves_disponibles = Eleve.objects.filter(utilise=False)
    if eleves_disponibles.exists():
        eleve_au_hasard = eleves_disponibles.order_by('?').first()
        eleve_au_hasard.utilise = True
        eleve_au_hasard.save()
        return HttpResponse(f'''<h1>L'élève au hasard est {eleve_au_hasard.nom} {eleve_au_hasard.prenom} et sa boite est {eleve_au_hasard.boite}. <a href="/eleve-au-hasard">Relancer le tirage</a></h1>''')
    else:
        return HttpResponse("<h1>Aucun élève disponible. Cela veut dire qu'ils ont tous eu leur ouverture (ou qu'un bug sauvage est apparu)</h1><p>Contactez Youri pour une remise à zéro d'utilisateurs ou des diagnostics plus poussés.</p>")

def eleve_au_hasard_apj(request):
    eleves_disponibles = Eleve.objects.filter(utilise=False, groupe_AP="JE")
    if eleves_disponibles.exists():
        eleve_au_hasard = eleves_disponibles.order_by('?').first()
        eleve_au_hasard.utilise = True
        eleve_au_hasard.save()
        return HttpResponse(f'''<h1>L'élève au hasard est {eleve_au_hasard.nom} {eleve_au_hasard.prenom} et sa boite est {eleve_au_hasard.boite}. <a href="/eleve-au-hasard">Relancer le tirage</a></h1>''')
    else:
        return HttpResponse("<h1>Aucun élève disponible. Cela veut dire qu'ils ont tous eu leur ouverture (ou qu'un bug sauvage est apparu)</h1><p>Contactez Youri pour une remise à zéro d'utilisateurs ou des diagnostics plus poussés.</p>")

def eleve_au_hasard_apm(request):
    eleves_disponibles = Eleve.objects.filter(utilise=False, groupe_AP="MA")
    if eleves_disponibles.exists():
        eleve_au_hasard = eleves_disponibles.order_by('?').first()
        eleve_au_hasard.utilise = True
        eleve_au_hasard.save()
        return HttpResponse(f'''<h1>L'élève au hasard est {eleve_au_hasard.nom} {eleve_au_hasard.prenom} et sa boite est {eleve_au_hasard.boite}. <a href="/eleve-au-hasard">Relancer le tirage</a></h1>''')
    else:
        return HttpResponse("<h1>Aucun élève disponible. Cela veut dire qu'ils ont tous eu leur ouverture (ou qu'un bug sauvage est apparu)</h1><p>Contactez Youri pour une remise à zéro d'utilisateurs ou des diagnostics plus poussés.</p>")

def cmb_eleves_aujourdhui(request):
    qterandom = random.randint(1, 4)
    return HttpResponse(f'''<h1>Aujourd'hui, { qterandom } élèves vont/va ouvrir leur/sa boite <a href="/eleve-au-hasard/">Cliquez ici pour en connaitre un.</a></h1>''')

def rootpage(request):
    return HttpResponse(f'''<header><h1>Calendrier de l'avent Noel 2024</h1><h3>Index des pages: <a href="combien/"><button>Combien d'élèves aujourd'hui</button></a>     <a href="eleve-au-hasard/"><button>Tirer un élève au hasard</button></a><a href="ap/mardi/au_hasard/"><button>Tirer au sort le mardi en AP</button></a><a href="ap/jeudi/au_hasard/"><button>Tirer au sort le jeudi en AP</button></a></h3></header><footer style=" vertical-align: bottom"><a href="admin"><button>/!\ADMIN/!\</button></a></footer>''')

