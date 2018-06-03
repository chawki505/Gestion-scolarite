from django.contrib import admin

from .models import *


# Register your models here.


class ReponsetInLine(admin.TabularInline):
    model = Reponse
    extra = 0


class MessageAdmin(admin.ModelAdmin):
    inlines = [ReponsetInLine]


admin.site.register(Message, MessageAdmin)
admin.site.register(Reponse)
