from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Etudiant(models.Model):
    user = models.OneToOneField('auth.User', related_name='etudiant')

    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)

    sexe = models.CharField(
        choices=(('Homme', 'Homme'), ('Femme', 'Femme')), max_length=256)

    adresse = models.CharField(max_length=256, blank=True, null=True)

    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=256, blank=True, null=True)
    nationalite = CountryField(blank=True, null=True)

    telephone = models.CharField(max_length=256, blank=True, null=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper() + " " + self.prenom.capitalize()

    class Meta:
        db_table = "etudiant"
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"


class Bac(models.Model):
    etudiant = models.OneToOneField(Etudiant, related_name='bac')

    numero = models.CharField(max_length=256)

    note = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(20)])

    MENTION = (('sans mention', 'Bac sans mention : entre 10 et 12/20'),
               ('mention assez bien', 'Bac avec mention assez bien : entre 12 et 14/20'),
               ('mention bien', 'Bac avec mention bien : entre 14 et 16/20'),
               ('mention très bien', 'Bac avec mention très bien : 16/20 et plus'))

    mention = models.CharField(choices=MENTION, max_length=256, default=MENTION[0])

    YEAR_CHOICES = []
    year = timezone.now().year
    for r in range(2000, (year + 1)):
        YEAR_CHOICES.append((r, r))

    session = models.IntegerField(choices=YEAR_CHOICES, default=year)

    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bac"
        verbose_name = "Bac"
        verbose_name_plural = "Bacs"

    def __str__(self):
        return self.numero


class Groupe(models.Model):
    nom = models.CharField(max_length=256)

    class Meta:
        db_table = "groupe"
        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"

    def __str__(self):
        return self.nom


class Inscription(models.Model):

    etudiant = models.ForeignKey(Etudiant, related_name='inscriptions')

    annee_universitaire = models.ForeignKey('etablissements.Annee_universitaire',
                                            related_name='inscriptions')

    parcours = models.ForeignKey('modules.Parcours', related_name='inscriptions')

    groupe = models.ForeignKey(Groupe, related_name='inscriptions', null=True)


    date_creation = models.DateTimeField(auto_now_add=True)

    categorie = models.CharField(choices=(('Inscription', 'Inscription'), ('Reinscription', 'Reinscription')),
                                 max_length=256, blank=True, null=True)

    def __str__(self):
        return self.etudiant.__str__() + " Specialité : " + self.parcours.__str__() + \
               " Année universitaire : " + self.annee_universitaire.nom

    class Meta:
        db_table = "inscription"
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"


class Note(models.Model):
    inscription = models.ForeignKey(Inscription, related_name='notes')
    module = models.ForeignKey('modules.Module', related_name='notes')

    noteCC = models.FloatField(null=True, blank=True)

    noteEF = models.FloatField(null=True, blank=True)

    noteER = models.FloatField(null=True, blank=True)

    moyenne1 = models.FloatField(null=True, blank=True, default=0)

    moyenne2 = models.FloatField(null=True, blank=True, default=0)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.inscription.etudiant.__str__() + " Module : " + self.module.nom

    def calcule_moyenne1(self):
        self.moyenne1 = round( (self.noteCC + self.noteEF) / 2, 2)
        self.save()

    def calcule_moyenne2(self):
        self.moyenne2 = round((self.noteCC + self.noteER) / 2, 2)
        self.save()

    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"
