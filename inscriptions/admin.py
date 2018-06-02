from django.contrib import admin
from .models import *


# Register your models here.


class BacInLine(admin.TabularInline):
    model = Bac
    max_num = 1
    min_num = 1


class InscriptionInLine(admin.TabularInline):
    model = Inscription
    max_num = 5
    extra = 0


class NoteInLine(admin.TabularInline):
    model = Note
    extra = 0


class EtudiantAdmin(admin.ModelAdmin):
    inlines = [BacInLine, InscriptionInLine]


class InscriptionAdmin(admin.ModelAdmin):
    inlines = [NoteInLine]


admin.site.register(Etudiant, EtudiantAdmin)
admin.site.register(Bac)
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Note)

admin.site.register(Groupe)
