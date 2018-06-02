from django.db import models


# Create your models here.

class Cycle(models.Model):
    nom = models.CharField(max_length=256)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = "cycle"
        verbose_name = "Cycle"
        verbose_name_plural = "Cycles"


class Specialite(models.Model):
    nom = models.CharField(max_length=256)
    departement = models.ForeignKey('etablissements.Departement', related_name='specialites')
    cycle = models.ForeignKey(Cycle, related_name='specialites')
    responsable = models.OneToOneField('enseignants.Enseignant', related_name='responsable_specialite')

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " cycle : " + self.cycle.nom

    class Meta:
        db_table = "specialite"
        verbose_name = "Specialite"
        verbose_name_plural = "Specialites"


class Parcours(models.Model):
    nom = models.CharField(max_length=256)
    specialite = models.ForeignKey(Specialite, related_name='parcours')
    responsable = models.OneToOneField('enseignants.Enseignant', related_name='responsable_parcours')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " Specialite : " + self.specialite.nom

    class Meta:
        db_table = "parcours"
        verbose_name = "Parcours"
        verbose_name_plural = "Parcours"


class Semestre(models.Model):
    nom = models.CharField(max_length=256)
    parcours = models.ForeignKey(Parcours, related_name='semestres')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + " Année specialité : " + self.parcours.nom

    class Meta:
        db_table = "semestre"
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"


class Unite(models.Model):
    nom = models.CharField(max_length=256)
    semestre = models.ForeignKey(Semestre, related_name='unites')
    enseignant = models.ForeignKey('enseignants.Enseignant', related_name='responsable_unite', null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "unite"
        verbose_name = "Unite"
        verbose_name_plural = "Unites"

    def __str__(self):
        return self.nom + ", Semestre : " + self.semestre.__str__()


class Module(models.Model):
    nom = models.CharField(max_length=256)
    unite = models.ForeignKey(Unite, related_name='modules')
    coefficient = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5)))
    enseignant = models.ForeignKey('enseignants.Enseignant', related_name='responsable_module', null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "module"
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.nom + ", Unite : " + self.unite.nom
