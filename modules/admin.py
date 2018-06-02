from django.contrib import admin

from .models import *


# Register your models here.


class SpecialiteInLine(admin.TabularInline):
    model = Specialite
    extra = 0


class ParcoursInLine(admin.TabularInline):
    model = Parcours
    extra = 0


class SemestreInLine(admin.TabularInline):
    model = Semestre
    extra = 0


class UniteInLine(admin.TabularInline):
    model = Unite
    extra = 0


class ModuleInLine(admin.TabularInline):
    model = Module
    extra = 0


class CycleAdmin(admin.ModelAdmin):
    inlines = [SpecialiteInLine]


class SpecialiteAdmin(admin.ModelAdmin):
    inlines = [ParcoursInLine]


class ParcoursAdmin(admin.ModelAdmin):
    inlines = [SemestreInLine]


class SemestreAdmin(admin.ModelAdmin):
    inlines = [UniteInLine]


class UniteAdmin(admin.ModelAdmin):
    inlines = [ModuleInLine]


admin.site.register(Cycle, CycleAdmin)
admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(Parcours, ParcoursAdmin)
admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Unite, UniteAdmin)
admin.site.register(Module)
