from django.db import models


# Create your models here.


class Cycle(models.Model):
    nom = models.CharField(max_length=256)
    departement = models.ForeignKey('etablissements.Departement')

    def __str__(self):
        return self.nom + " Departement : " + self.departement.nom

    class Meta:
        db_table = "cycle"
        verbose_name = "Cycle"
        verbose_name_plural = "Cycles"


class Specialite(models.Model):
    nom = models.CharField(max_length=256)
    cycle = models.ForeignKey(Cycle, related_name='specialites')

    def __str__(self):
        return self.nom + " cycle : " + self.cycle.nom

    class Meta:
        db_table = "specialite"
        verbose_name = "Specialite"
        verbose_name_plural = "Specialites"


class Annee_specialite(models.Model):
    nom = models.CharField(max_length=256)
    specialite = models.ForeignKey(Specialite, related_name='annees_specialite')

    def __str__(self):
        return self.nom + " Specialité : " + self.specialite.nom

    class Meta:
        db_table = "annee_specialite"
        verbose_name = "Annee_specialite"
        verbose_name_plural = "Annees_specialite"


class Semestre(models.Model):
    nom = models.CharField(max_length=256)
    annee_specialite = models.ForeignKey(Annee_specialite, related_name='semestres_annee_specialite')

    def __str__(self):
        return self.nom + " Année specialité : " + self.annee_specialite.nom

    class Meta:
        db_table = "semestre"
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"


class Unite(models.Model):
    nom = models.CharField(max_length=256)
    semestre = models.ForeignKey(Semestre, related_name='unites_semestre')

    class Meta:
        db_table = "unite"
        verbose_name = "Unite"
        verbose_name_plural = "Unites"

    def __str__(self):
        return self.nom + ", Semestre : " + self.semestre.__str__()


class Module(models.Model):
    nom = models.CharField(max_length=256)
    unite = models.ForeignKey(Unite, related_name='modules_unite')
    coefficient = models.IntegerField()

    class Meta:
        db_table = "module"
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.nom + ", Unite : " + self.unite.nom
