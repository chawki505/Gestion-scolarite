from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Annee_universitaire)
admin.site.register(Etablisement)
admin.site.register(Faculte)
admin.site.register(Domaine)
admin.site.register(Departement)
admin.site.register(Cycle)
admin.site.register(Specialite)
admin.site.register(Annee_specialite)
admin.site.register(Semestre)

admin.site.register(Etudiant)
admin.site.register(Bac)
admin.site.register(Inscription)
