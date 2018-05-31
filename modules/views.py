from django.shortcuts import render, redirect

from .models import *

from inscriptions.models import Note

from etablissements.models import Annee_universitaire


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

        notes = module.notes_module.all()

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

        unite = Unite.objects.get(pk=pk)

        modules = unite.modules_unite.all()

        annee_universitaire = Annee_universitaire.objects.all().last()

        context = {
            'unite': unite,
            'annee_universitaire': annee_universitaire,
            'modules': modules,
        }

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
