from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *


# Create your views here.


def dashboard_liste_inscriptions(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        inscriptions = Inscription.objects.all()

        return render(request, 'inscriptions/liste_inscriptions.html',
                      {'inscriptions': inscriptions})

    else:
        return redirect('login_account')


def dashboard_detail_inscription(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        inscription = Inscription.objects.get(pk=pk)
        semestres = inscription.annee_specialite.semestres_annee_specialite.all()

        return render(request, 'inscriptions/detail_inscription.html',
                      {'inscription': inscription,
                       'semestres': semestres})

    else:
        return redirect('login_account')


def dashboard_liste_etudiants(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        etudiants = Etudiant.objects.all()

        return render(request, 'inscriptions/liste_etudiants.html',
                      {'etudiants': etudiants})

    else:
        return redirect('login_account')


def dashboard_detail_etudiant(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        etudiant = Etudiant.objects.get(pk=pk)
        inscriptions = etudiant.inscriptions_etudiant.all()

        contexe = {'etudiant': etudiant,
                   'inscriptions': inscriptions,

                   }

        return render(request, 'inscriptions/detail_etudiant.html', contexe)

    else:
        return redirect('login_account')


def dashboard_liste_bac(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        bacs = Bac.objects.all()

        return render(request, 'inscriptions/liste_bacs.html', {'bacs': bacs})

    else:
        return redirect('login_account')


def attestation_inscription(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        inscription = Inscription.objects.get(pk=pk)

        return render(request, 'inscriptions/doc/attestation_inscription.html', {'inscription': inscription})
    else:
        return redirect('login_account')


def certificat_scolarite(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        inscription = Inscription.objects.get(pk=pk)
        return render(request, 'inscriptions/doc/certificat_scolarite.html', {'inscription': inscription})

    else:
        return redirect('login_account')
