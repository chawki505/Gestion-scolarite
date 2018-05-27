from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Annee_universitaire(models.Model):
    nom = models.CharField(max_length=256)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "annee_universitaire"
        verbose_name = "Annee_universitaire"
        verbose_name_plural = "Annees_universitaire"


class Etablisement(models.Model):
    nom = models.CharField(max_length=256)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "etablisement"
        verbose_name = "Etablisement"
        verbose_name_plural = "Etablisements"


class Faculte(models.Model):
    nom = models.CharField(max_length=256)
    etablissement = models.ForeignKey(Etablisement)

    def __str__(self):
        return self.nom + " Etablisement : " + self.etablissement.nom

    class Meta:
        db_table = "faculte"
        verbose_name = "Faculte"
        verbose_name_plural = "Facultes"


class Domaine(models.Model):
    nom = models.CharField(max_length=256)
    faculte = models.ForeignKey(Faculte)

    def __str__(self):
        return self.nom + " Faculte : " + self.faculte.nom

    class Meta:
        db_table = "domaine"
        verbose_name = "Domaine"
        verbose_name_plural = "Domaines"


class Departement(models.Model):
    nom = models.CharField(max_length=256)
    domaine = models.ForeignKey(Domaine)

    def __str__(self):
        return self.nom + " Domaine : " + self.domaine.nom

    class Meta:
        db_table = "departement"
        verbose_name = "Departement"
        verbose_name_plural = "Departements"


class Cycle(models.Model):
    nom = models.CharField(max_length=256)
    departement = models.ForeignKey(Departement)

    def __str__(self):
        return self.nom + " Departement : " + self.departement.nom

    class Meta:
        db_table = "cycle"
        verbose_name = "Cycle"
        verbose_name_plural = "Cycles"


class Specialite(models.Model):
    nom = models.CharField(max_length=256)
    cycle = models.ForeignKey(Cycle)

    def __str__(self):
        return self.nom + " cycle : " + self.cycle.nom

    class Meta:
        db_table = "specialite"
        verbose_name = "Specialite"
        verbose_name_plural = "Specialites"


class Annee_specialite(models.Model):
    nom = models.CharField(max_length=256)
    specialite = models.ForeignKey(Specialite)

    def __str__(self):
        return self.nom + " Specialité : " + self.specialite.nom

    class Meta:
        db_table = "annee_specialite"
        verbose_name = "Annee_specialite"
        verbose_name_plural = "Annees_specialite"


class Semestre(models.Model):
    nom = models.CharField(max_length=256)
    annee_specialite = models.ForeignKey(Annee_specialite)

    def __str__(self):
        return self.nom + " Année specialité : " + self.annee_specialite.nom

    class Meta:
        db_table = "semestre"
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"


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
    etudiant = models.ForeignKey(Etudiant)
    annee_universitaire = models.ForeignKey(Annee_universitaire)
    annee_specialite = models.ForeignKey(Annee_specialite)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.etudiant.__str__() + " Specialité : " + self.annee_specialite.__str__() + " Année universitaire : " + self.annee_universitaire.nom

    class Meta:
        db_table = "etudiant_inscription_specialite"
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"
