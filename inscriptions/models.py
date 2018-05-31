from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Etudiant(models.Model):
    user = models.OneToOneField('auth.User')
    sexe = models.CharField(
        choices=(('Homme', 'Homme'), ('Femme', 'Femme')), max_length=100, blank=True)
    adresse = models.CharField(max_length=256)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=256, blank=True, null=True)
    nationalite = CountryField(blank=True)

    telephone = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        db_table = "etudiant"
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"


class Bac(models.Model):
    etudiant = models.OneToOneField(Etudiant)
    date_ajout = models.DateTimeField(auto_now_add=True)

    numero = models.CharField(max_length=100)

    note = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    MENTION = (('sans mention', 'Bac sans mention : entre 10 et 12/20'),
               ('mention assez bien', 'Bac avec mention assez bien : entre 12 et 14/20'),
               ('mention bien', 'Bac avec mention bien : entre 14 et 16/20'),
               ('mention très bien', 'Bac avec mention très bien : 16/20 et plus'))

    mention = models.CharField(choices=MENTION, max_length=100)

    YEAR_CHOICES = []
    year = timezone.now().year
    for r in range(2000, (year + 1)):
        YEAR_CHOICES.append((r, r))

    session = models.IntegerField(choices=YEAR_CHOICES, default=year)

    class Meta:
        db_table = "etudiant_bac"
        verbose_name = "Bac"
        verbose_name_plural = "Bacs"

    def __str__(self):
        return self.numero


class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, related_name='inscriptions_etudiant')
    annee_universitaire = models.ForeignKey('etablissements.Annee_universitaire',
                                            related_name='inscriptions_annee_universitaire')
    annee_specialite = models.ForeignKey('modules.Annee_specialite')
    date_inscription = models.DateTimeField(auto_now_add=True)
    categorie = models.CharField(choices=(('Inscription', 'Inscription'), ('Reinscription', 'Reinscription')),
                                 max_length=100, blank=True)

    def __str__(self):
        return self.etudiant.__str__() + " Specialité : " + self.annee_specialite.__str__() + \
               " Année universitaire : " + self.annee_universitaire.nom

    class Meta:
        db_table = "etudiant_inscription"
        verbose_name = "inscription"
        verbose_name_plural = "inscriptions"


class Note(models.Model):
    inscription_etudiant = models.ForeignKey(Inscription, related_name='notes_inscription_etudiant', null=True,
                                             blank=True)
    module = models.ForeignKey('modules.Module', related_name='notes_module')
    note = models.FloatField()
    annee_universitaire = models.ForeignKey('etablissements.Annee_universitaire',
                                            related_name='notes_annee_universitaire')

    def __str__(self):
        return self.inscription_etudiant.etudiant.__str__() + " Module : " + self.module.nom + \
               ", Note : " + self.note.__str__()

    class Meta:
        db_table = "inscription_etudiant_module_note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"
