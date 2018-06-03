from django import forms

from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('titre', 'destinataire', 'texte',)


class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ('titre', 'texte',)
