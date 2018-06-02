from django.db import models

from django_countries.fields import CountryField


# Create your models here.


class Enseignant(models.Model):
    user = models.OneToOneField('auth.User', related_name='enseignant')
    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)

    sexe = models.CharField(choices=(('Homme', 'Homme'), ('Femme', 'Femme')), max_length=256)

    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance = models.CharField(max_length=256, blank=True, null=True)

    GRADE = (('PR', 'Professeur'),
             ('MCA', 'Maitre de conference A'),
             ('MCB', 'Maitre de conference B'),
             ('MAA', 'Maitre assistant A'),
             ('MAB', 'Maitre assistant B'))

    grade = models.CharField(choices=GRADE, max_length=256)

    nationalite = CountryField(blank=True, null=True)

    adresse = models.CharField(max_length=256, blank=True, null=True)
    telephone = models.CharField(max_length=256, blank=True, null=True)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper() + " " + self.prenom.capitalize() + " " + self.grade

    class Meta:
        db_table = "enseignant"
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"
