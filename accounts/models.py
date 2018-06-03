from django.db import models

from django.utils import timezone


# Create your models here.


class Message(models.Model):
    auteur = models.ForeignKey('auth.User', related_name='messages_envoyer')
    titre = models.CharField(max_length=250)
    destinataire = models.ForeignKey('auth.User', related_name='messages_recu')
    created_date = models.DateTimeField(auto_now_add=True)

    texte = models.TextField()

    def __str__(self):
        return self.titre

    class Meta:
        db_table = "message"
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Reponse(models.Model):
    message = models.ForeignKey(Message, related_name='reponses')
    auteur = models.ForeignKey('auth.User', related_name='reponses_envoyer')
    titre = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)

    texte = models.TextField()

    def __str__(self):
        return self.titre

    class Meta:
        db_table = "reponse"
        verbose_name = "Reponse"
        verbose_name_plural = "Reponses"
