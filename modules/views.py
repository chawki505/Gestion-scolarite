from django.shortcuts import render, redirect

from .models import *

from inscriptions.models import *

from inscriptions.models import Note

from etablissements.models import Annee_universitaire

from django.db.models import Q

# Create your views here.


last_annee_univ = Annee_universitaire.objects.get(nom__contains=timezone.now().year)


def liste_modules(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        modules = Module.objects.all()

        contexe = {'modules': modules}
        return render(request, 'modules/liste_modules.html', contexe)
    else:
        return redirect('login_account')


def pv_module(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get module
        module = Module.objects.get(pk=pk)

        # get all notes module
        notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

        # get inscriptions modules
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=module.unite.semestre.parcours))

        notesCC = notes.filter(Q(categorie='CC') & Q(inscription__in=inscriptions))

        notesEF = notes.filter(Q(categorie='EF') & Q(inscription__in=inscriptions))

        student_list = []

        for inscription in inscriptions:
            # counter and dictionary initialisation

            moyenne_dict = dict()
            noteCC = notesCC.get(inscription=inscription).note
            noteEF = notesEF.get(inscription=inscription).note

            moyenne = (noteCC + noteEF) / 2

            moyenne_dict['numero'] = inscription.etudiant.id
            moyenne_dict['nom'] = inscription.etudiant.nom.upper()
            moyenne_dict['prenom'] = inscription.etudiant.prenom.capitalize()
            moyenne_dict['groupe'] = inscription.groupe.nom
            moyenne_dict['CC'] = noteCC
            moyenne_dict['EF'] = noteEF
            moyenne_dict['moyenne'] = moyenne

            student_list.append(moyenne_dict)

        context = {
            'module': module,
            'notes': student_list,
        }

        return render(request, 'modules/pv_module.html', context)
    else:
        return redirect('login_account')


def liste_unites(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        unites = Unite.objects.all()
        contexe = {'unites': unites}
        return render(request, 'modules/liste_unites.html', contexe)
    else:
        return redirect('login_account')


def pv_unite(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # getting the unity
        unite = Unite.objects.get(pk=pk)

        # getting all modules
        modules = unite.modules.all()

        # get inscriptions unite
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=unite.semestre.parcours))

        student_list = []

        for inscription in inscriptions:
            # counter and dictionary initialisation
            moyenne = 0
            coef = 0
            moyenne_dict = dict()
            # build the dictionary
            moyenne_dict['numero'] = inscription.etudiant.id
            moyenne_dict['nom'] = inscription.etudiant.nom.upper()
            moyenne_dict['prenom'] = inscription.etudiant.prenom.capitalize()
            moyenne_dict['groupe'] = inscription.groupe.nom

            # unit average computation
            for module in modules:
                notes = Note.objects.filter(Q(inscription=inscription) & Q(module=module))
                noteCC = notes.get(categorie='CC')
                noteEF = notes.get(categorie='EF')
                # if the student has this module

                if noteCC is not None and noteEF is not None:
                    moyenne_module = (noteCC.note + noteEF.note) / 2
                    moyenne += moyenne_module * module.coefficient  # counting
                    coef += module.coefficient
                    moyenne_dict[module.nom] = moyenne_module

            # calculate the average
            moyenne = round(moyenne / coef, 2)

            moyenne_dict['moyenne'] = moyenne

            # add it on the array
            student_list.append(moyenne_dict)

        context = {'unite': unite,
                   'notes': student_list, }

        return render(request, 'modules/pv_unite.html', context)
    else:
        return redirect('login_account')


def liste_semestres(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        semestres = Semestre.objects.all()
        contexe = {'semestres': semestres}
        return render(request, 'modules/liste_semestres.html', contexe)
    else:
        return redirect('login_account')


def calcule_moyenne_module(module, inscription):
    # get all notes module
    notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ, inscription=inscription)

    # filter note cc and ef
    noteCC = notes.get(categorie='CC')
    noteEF = notes.get(categorie='EF')

    moyenne = round((noteCC.note + noteEF.note) / 2, 2)

    return moyenne


def pv_semestre(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get semestres
        semestre = Semestre.objects.get(pk=pk)

        # get all unite semestre
        unites = semestre.unites.all()

        # get inscriptions semestre
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=semestre.parcours))

        student_list = []

        for inscription in inscriptions:
            moyenne_semestre = 0
            coef_semestre = 0
            moyenne_semestre_dict = dict()

            # build the dictionary
            moyenne_semestre_dict['numero'] = inscription.etudiant.id
            moyenne_semestre_dict['nom'] = inscription.etudiant.nom.upper()
            moyenne_semestre_dict['prenom'] = inscription.etudiant.prenom.capitalize()
            moyenne_semestre_dict['groupe'] = inscription.groupe.nom

            for unite in unites:

                for module in unite.modules.all():
                    if module.nom == 'Projet':
                        note = Note.objects.get(Q(inscription=inscription) & Q(module=module))
                        moyenne_semestre += note.note * module.coefficient  # counting
                        coef_semestre += module.coefficient

                    else:
                        notes = Note.objects.filter(Q(inscription=inscription) & Q(module=module))
                        noteCC = notes.get(categorie='CC')
                        noteEF = notes.get(categorie='EF')
                        # if the student has this module

                        if noteCC is not None and noteEF is not None:
                            moyenne_module = (noteCC.note + noteEF.note) / 2
                            moyenne_semestre += moyenne_module * module.coefficient  # counting
                            coef_semestre += module.coefficient
                        else:
                            moyenne_module = 0
                            moyenne_semestre += moyenne_module * module.coefficient  # counting
                            coef_semestre += module.coefficient

            moyenne_semestre = round((moyenne_semestre / coef_semestre), 2)
            moyenne_semestre_dict['moyenne'] = moyenne_semestre

            print(moyenne_semestre_dict)
            # add it on the array
            student_list.append(moyenne_semestre_dict)

        contexe = {'semestre': semestre,
                   'moyennes': student_list, }

        return render(request, 'modules/pv_semestre.html', contexe)
    else:
        return redirect('login_account')
