from django.contrib import admin

from .models import *

from modules.models import Module


# Register your models here.


class ModulelInLine(admin.StackedInline):
    model = Module
    extra = 0


class EnseignantAdmin(admin.ModelAdmin):
    inlines = [ModulelInLine]


admin.site.register(Enseignant,EnseignantAdmin)




