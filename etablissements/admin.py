from django.contrib import admin

from .models import *


class DepatementInLine(admin.TabularInline):
    model = Departement
    extra = 0


class DomaineAdmin(admin.ModelAdmin):
    inlines = [DepatementInLine]


# Register your models here.
admin.site.register(Annee_universitaire)
admin.site.register(Etablisement)
admin.site.register(Faculte)
admin.site.register(Domaine, DomaineAdmin)
admin.site.register(Departement)
