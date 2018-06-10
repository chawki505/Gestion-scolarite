from django.shortcuts import render, redirect

from .models import *

from inscriptions.models import *

from inscriptions.models import Note

from etablissements.models import Annee_universitaire

from django.db.models import Q

# Create your views here.


''''Variable partager'''
# get last annee universitaire
last_annee_univ = Annee_universitaire.objects.get(nom__contains=timezone.now().year)


# affichage de la liste des modules
def liste_modules(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        modules = Module.objects.all()

        contexe = {
            'modules': modules,
        }
        return render(request, 'modules/liste_modules.html', contexe)

    elif request.user.is_authenticated and request.user.groups.filter(name='Enseignants').exists():

        modules = Module.objects.filter(enseignant__user=request.user)

        contexe = {
            'modules': modules,
        }
        return render(request, 'modules/liste_modules.html', contexe)

    else:
        return redirect('login_account')


# affichage de la liste des notes du module
def liste_notes_module(request, pk):
    if request.user.is_authenticated and (
            request.user.groups.filter(name='Administrateur').exists() or
            request.user.groups.filter(name='Enseignants').exists()):

        # get module
        module = Module.objects.get(pk=pk)

        # get all notes module
        notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

        for note in notes:
            note.calcule_moyenne1()
            if note.noteER is not None:
                note.calcule_moyenne2()

        # get inscriptions modules
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=module.unite.semestre.parcours))

        # filtre notes
        notes = notes.filter(inscription__in=inscriptions)

        student_list = []

        for inscription in inscriptions:
            # counter and dictionary initialisation

            moyenne_dict = dict()

            noteCC = notes.get(inscription=inscription).noteCC
            noteEF = notes.get(inscription=inscription).noteEF

            moyenne = notes.get(inscription=inscription).moyenne1

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

        return render(request, 'modules/listes_notes_module.html', context)
    else:
        return redirect('login_account')


# affichage du pv du module
def pv_module(request, pk):
    if request.user.is_authenticated and (
            request.user.groups.filter(name='Administrateur').exists() or request.user.groups.filter(
        name='Enseignants').exists()):

        # get module
        module = Module.objects.get(pk=pk)

        # get all notes module
        notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

        for note in notes:
            note.calcule_moyenne1()
            if note.noteER is not None:
                note.calcule_moyenne2()

        # get inscriptions modules
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=module.unite.semestre.parcours))

        # filtre notes
        notes = notes.filter(inscription__in=inscriptions)

        student_list = []

        for inscription in inscriptions:
            # counter and dictionary initialisation

            moyenne_dict = dict()
            noteCC = notes.get(inscription=inscription).noteCC
            noteEF = notes.get(inscription=inscription).noteEF

            moyenne = notes.get(inscription=inscription).moyenne1

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

        return render(request, 'modules/doc/pv_module.html', context)
    else:
        return redirect('login_account')


# affichage de la liste des unite
def liste_unites(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        unites = Unite.objects.all()

        contexe = {
            'unites': unites,
        }
        return render(request, 'modules/liste_unites.html', contexe)

    elif request.user.is_authenticated and request.user.groups.filter(name='Enseignants').exists():
        unites = Unite.objects.filter(enseignant__user=request.user)

        contexe = {
            'unites': unites,
        }
        return render(request, 'modules/liste_unites.html', contexe)

    else:
        return redirect('login_account')


# affichage des notes unite
def liste_notes_unite(request, pk):
    if request.user.is_authenticated and \
            (request.user.groups.filter(name='Administrateur').exists() or
             request.user.groups.filter(name='Enseignants').exists()):

        # get unite
        unite = Unite.objects.get(pk=pk)

        # getting all modules unite
        modules = unite.modules.all()

        # get all inscriptions unite
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=unite.semestre.parcours))

        # tab etudiant
        student_list = []

        # parcours pour chaque inscription
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

                # get all notes module
                notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

                # calcule moyenne module
                for note in notes:
                    note.calcule_moyenne1()
                    if note.noteER is not None:
                        note.calcule_moyenne2()

                # get moyenne module
                moyenne_module = notes.get(inscription=inscription).moyenne1

                # somme all moyenne module unite
                moyenne += moyenne_module * module.coefficient

                # somme all coef module unite
                coef += module.coefficient

                # save moyenne module unite in dico
                moyenne_dict[module.nom] = moyenne_module

            # calcule moyenne unite
            moyenne = round(moyenne / coef, 2)

            # save moyenne unite
            moyenne_dict['moyenne'] = moyenne

            # add it on the tab student
            student_list.append(moyenne_dict)

        context = {
            'unite': unite,
            'notes': student_list,
        }

        return render(request, 'modules/liste_notes_unite.html', context)
    else:
        return redirect('login_account')


# affichage du pv
def pv_unite(request, pk):
    if request.user.is_authenticated and (
            request.user.groups.filter(name='Administrateur').exists() or
            request.user.groups.filter(name='Enseignants').exists()):
        # get unite
        unite = Unite.objects.get(pk=pk)

        # getting all modules unite
        modules = unite.modules.all()

        # get all inscriptions unite
        inscriptions = Inscription.objects.filter(
            Q(annee_universitaire=last_annee_univ) & Q(parcours=unite.semestre.parcours))

        # tab etudiant
        student_list = []

        # parcours pour chaque inscription
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

                # get all notes module
                notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

                # calcule moyenne module
                for note in notes:
                    note.calcule_moyenne1()
                    if note.noteER is not None:
                        note.calcule_moyenne2()

                # get moyenne module
                moyenne_module = notes.get(inscription=inscription).moyenne1

                # somme all moyenne module unite
                moyenne += moyenne_module * module.coefficient

                # somme all coef module unite
                coef += module.coefficient

                # save moyenne module unite in dico
                moyenne_dict[module.nom] = moyenne_module

            # calcule moyenne unite
            moyenne = round(moyenne / coef, 2)

            # save moyenne unite
            moyenne_dict['moyenne'] = moyenne

            # add it on the tab student
            student_list.append(moyenne_dict)

        context = {
            'unite': unite,
            'notes': student_list,
        }

        return render(request, 'modules/doc/pv_unite.html', context)
    else:
        return redirect('login_account')


# # affichage du pv
# def pv_unite(request, pk):
#     if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
#
#         # getting the unity
#         unite = Unite.objects.get(pk=pk)
#
#         # getting all modules
#         modules = unite.modules.all()
#
#         # get inscriptions unite
#         inscriptions = Inscription.objects.filter(
#             Q(annee_universitaire=last_annee_univ) & Q(parcours=unite.semestre.parcours))
#
#         student_list = []
#
#         for inscription in inscriptions:
#             # counter and dictionary initialisation
#             moyenne = 0
#             coef = 0
#             moyenne_dict = dict()
#             # build the dictionary
#             moyenne_dict['numero'] = inscription.etudiant.id
#             moyenne_dict['nom'] = inscription.etudiant.nom.upper()
#             moyenne_dict['prenom'] = inscription.etudiant.prenom.capitalize()
#             moyenne_dict['groupe'] = inscription.groupe.nom
#
#             # unit average computation
#             for module in modules:
#                 notes = Note.objects.filter(Q(inscription=inscription) & Q(module=module))
#                 noteCC = notes.get(categorie='CC')
#                 noteEF = notes.get(categorie='EF')
#                 # if the student has this module
#
#                 if noteCC is not None and noteEF is not None:
#                     moyenne_module = (noteCC.note + noteEF.note) / 2
#                     moyenne += moyenne_module * module.coefficient  # counting
#                     coef += module.coefficient
#                     moyenne_dict[module.nom] = moyenne_module
#
#             # calculate the average
#             moyenne = round(moyenne / coef, 2)
#
#             moyenne_dict['moyenne'] = moyenne
#
#             # add it on the array
#             student_list.append(moyenne_dict)
#
#         context = {'unite': unite,
#                    'notes': student_list, }
#
#         return render(request, 'modules/doc/pv_unite.html', context)
#     else:
#         return redirect('login_account')


# affichage de la liste des semestres
def liste_semestres(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        semestres = Semestre.objects.all()
        contexe = {
            'semestres': semestres,
        }
        return render(request, 'modules/liste_semestres.html', contexe)

    elif request.user.is_authenticated and request.user.groups.filter(name='Enseignants').exists():

        semestres = Semestre.objects.filter(parcours__responsable__user=request.user)

        contexe = {
            'semestres': semestres,
        }
        return render(request, 'modules/liste_semestres.html', contexe)


    else:
        return redirect('login_account')


# affichage des notes du semestre
def liste_notes_semestre(request, pk):
    if request.user.is_authenticated and (
            request.user.groups.filter(name='Administrateur').exists() or
            request.user.groups.filter(name='Enseignants').exists()):
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
                # counter and dictionary initialisation
                moyenne_unite = 0
                coef_unite = 0

                for module in unite.modules.all():


                    # get all notes module
                    notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

                    # calcule moyenne module
                    for note in notes:
                        note.calcule_moyenne1()

                    # get moyenne module
                    moyenne_module = notes.get(inscription=inscription).moyenne1

                    # somme all moyenne module unite
                    moyenne_unite += moyenne_module * module.coefficient

                    # somme all coef module unite
                    coef_unite += module.coefficient

                    # save moyenne module unite in dico
                    moyenne_semestre_dict[module.nom] = moyenne_module

                # somme moyenne semestre
                moyenne_semestre += moyenne_unite

                # somme coef somestre
                coef_semestre += coef_unite

                # calcule moyenne unite
                moyenne_unite = round(moyenne_unite / coef_unite, 2)

                # save moyenne unite
                moyenne_semestre_dict[unite] = moyenne_unite

            moyenne_semestre = round((moyenne_semestre / coef_semestre), 2)
            moyenne_semestre_dict['moyenne'] = moyenne_semestre

            # add it on the array
            student_list.append(moyenne_semestre_dict)

        contexe = {
            'semestre': semestre,
            'unites': unites,
            'moyennes': student_list,
        }

        return render(request, 'modules/liste_notes_semestre.html', contexe)

    else:
        return redirect('login_account')


# affichage du pv
def pv_semestre(request, pk):
    if request.user.is_authenticated and (
            request.user.groups.filter(name='Administrateur').exists() or
            request.user.groups.filter(name='Enseignants').exists()):
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
                # counter and dictionary initialisation
                moyenne_unite = 0
                coef_unite = 0

                for module in unite.modules.all():


                    # get all notes module
                    notes = module.notes.filter(inscription__annee_universitaire=last_annee_univ)

                    # calcule moyenne module
                    for note in notes:
                        note.calcule_moyenne1()

                    # get moyenne module
                    moyenne_module = notes.get(inscription=inscription).moyenne1

                    # somme all moyenne module unite
                    moyenne_unite += moyenne_module * module.coefficient

                    # somme all coef module unite
                    coef_unite += module.coefficient

                    # save moyenne module unite in dico
                    moyenne_semestre_dict[module.nom] = moyenne_module

                # somme moyenne semestre
                moyenne_semestre += moyenne_unite

                # somme coef somestre
                coef_semestre += coef_unite

                # calcule moyenne unite
                moyenne_unite = round(moyenne_unite / coef_unite, 2)

                # save moyenne unite
                moyenne_semestre_dict[unite] = moyenne_unite

            moyenne_semestre = round((moyenne_semestre / coef_semestre), 2)
            moyenne_semestre_dict['moyenne'] = moyenne_semestre

            # add it on the array
            student_list.append(moyenne_semestre_dict)

        contexe = {
            'semestre': semestre,
            'unites': unites,
            'moyennes': student_list,
        }

        return render(request, 'modules/doc/pv_semestre.html', contexe)
    else:
        return redirect('login_account')

# # affichage du pv
# def pv_semestre(request, pk):
#     if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
#
#         # get semestres
#         semestre = Semestre.objects.get(pk=pk)
#
#         # get all unite semestre
#         unites = semestre.unites.all()
#
#         # get inscriptions semestre
#         inscriptions = Inscription.objects.filter(
#             Q(annee_universitaire=last_annee_univ) & Q(parcours=semestre.parcours))
#
#         student_list = []
#
#         for inscription in inscriptions:
#             moyenne_semestre = 0
#             coef_semestre = 0
#             moyenne_semestre_dict = dict()
#
#             # build the dictionary
#             moyenne_semestre_dict['numero'] = inscription.etudiant.id
#             moyenne_semestre_dict['nom'] = inscription.etudiant.nom.upper()
#             moyenne_semestre_dict['prenom'] = inscription.etudiant.prenom.capitalize()
#             moyenne_semestre_dict['groupe'] = inscription.groupe.nom
#
#             for unite in unites:
#
#                 for module in unite.modules.all():
#                     if module.nom == 'Projet':
#                         note = Note.objects.get(Q(inscription=inscription) & Q(module=module))
#                         moyenne_semestre += note.note * module.coefficient  # counting
#                         coef_semestre += module.coefficient
#
#                     else:
#                         notes = Note.objects.filter(Q(inscription=inscription) & Q(module=module))
#                         noteCC = notes.get(categorie='CC')
#                         noteEF = notes.get(categorie='EF')
#                         # if the student has this module
#
#                         if noteCC is not None and noteEF is not None:
#                             moyenne_module = (noteCC.note + noteEF.note) / 2
#                             moyenne_semestre += moyenne_module * module.coefficient  # counting
#                             coef_semestre += module.coefficient
#                         else:
#                             moyenne_module = 0
#                             moyenne_semestre += moyenne_module * module.coefficient  # counting
#                             coef_semestre += module.coefficient
#
#             moyenne_semestre = round((moyenne_semestre / coef_semestre), 2)
#             moyenne_semestre_dict['moyenne'] = moyenne_semestre
#
#             print(moyenne_semestre_dict)
#             # add it on the array
#             student_list.append(moyenne_semestre_dict)
#
#         contexe = {
#             'semestre': semestre,
#             'moyennes': student_list,
#         }
#
#         return render(request, 'modules/doc/pv_semestre.html', contexe)
#     else:
#         return redirect('login_account')
