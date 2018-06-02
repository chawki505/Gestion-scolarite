from django.db import models


# Create your models here.


# Create your models here.
class Annee_universitaire(models.Model):
    nom = models.CharField(max_length=256)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "annee_universitaire"
        verbose_name = "Annee universitaire"
        verbose_name_plural = "Annees universitaire"


class Etablisement(models.Model):
    nom = models.CharField(max_length=256)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "etablisement"
        verbose_name = "Etablisement"
        verbose_name_plural = "Etablisements"


class Faculte(models.Model):
    nom = models.CharField(max_length=256)
    etablissement = models.ForeignKey(Etablisement, related_name='facultes')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " Etablisement : " + self.etablissement.nom

    class Meta:
        db_table = "faculte"
        verbose_name = "Faculte"
        verbose_name_plural = "Facultes"


class Domaine(models.Model):
    nom = models.CharField(max_length=256)
    faculte = models.ForeignKey(Faculte, related_name='domaines')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " Faculte : " + self.faculte.nom

    class Meta:
        db_table = "domaine"
        verbose_name = "Domaine"
        verbose_name_plural = "Domaines"


class Departement(models.Model):
    nom = models.CharField(max_length=256)
    domaine = models.ForeignKey(Domaine, related_name='departements')

    chef = models.OneToOneField('enseignants.Enseignant', related_name='chaf_departement')

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " Domaine : " + self.domaine.nom

    class Meta:
        db_table = "departement"
        verbose_name = "Departement"
        verbose_name_plural = "Departements"
