from django.shortcuts import render, redirect

from .models import *

from inscriptions.models import *

from inscriptions.models import Note

from etablissements.models import Annee_universitaire

from django.db.models import Q


# Create your views here.


def liste_modules(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        modules = Module.objects.all()
        contexe = {'modules': modules}
        return render(request, 'modules/liste_modules.html', contexe)
    else:
        return redirect('login_account')


def pv_module(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        module = Module.objects.get(pk=pk)

        notes = module.notes.all()

        context = {
            'notes': notes,
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

        # getting the inscriptions
        annee_univ = Annee_universitaire.objects.all().last()
        inscriptions = Inscription.objects.filter(annee_universitaire=annee_univ)

        student_list = []
        for inscription in inscriptions:
            # counter and dictionary initialisation
            moyenne = 0
            coef = 0
            moyenne_dict = dict()

            # unit average computation
            for module in modules:
                note = Note.objects.get(Q(inscription=inscription) & Q(module=module))
                # if the student has this module
                if note is not None and note.note is not None:
                    moyenne += note.note * module.coefficient  # counting
                    coef += module.coefficient

            # calculate the average
            moyenne = moyenne / coef
            # build the dictionary
            moyenne_dict['etudiant'] = inscription.etudiant
            moyenne_dict['moyenne'] = moyenne
            # add it on the array
            student_list.append(moyenne_dict)
        print(student_list)
        context = {'student': student_list}
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
