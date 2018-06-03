from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from etablissements.models import Annee_universitaire


# Create your views here.


def dashboard_liste_inscriptions(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get only inscriptions in last annee univ
        annee_univ = Annee_universitaire.objects.get(nom__contains=timezone.now().year)
        inscriptions = Inscription.objects.filter(annee_universitaire=annee_univ)

        return render(request, 'inscriptions/liste_inscriptions.html',
                      {'inscriptions': inscriptions})

    else:
        return redirect('login_account')


def dashboard_detail_inscription(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        inscription = Inscription.objects.get(pk=pk)

        semestres = inscription.parcours.semestres.all()

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
    if request.user.is_authenticated:

        if request.user.groups.filter(name='Administrateur').exists() or \
                (request.user.groups.filter(name='Etudiants').exists() and
                 get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            etudiant = Etudiant.objects.get(pk=pk)
            inscriptions = etudiant.inscriptions.all().order_by('-annee_universitaire__nom')

            bac = etudiant.bac

            contexe = {'etudiant': etudiant,
                       'inscriptions': inscriptions,
                       'bac': bac,
                       }
            return render(request, 'inscriptions/detail_etudiant.html', contexe)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


def dashboard_liste_bac(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        bacs = Bac.objects.all()

        return render(request, 'inscriptions/liste_bacs.html', {'bacs': bacs})

    else:
        return redirect('login_account')


def attestation_inscription(request, pk):
    if request.user.is_authenticated:

        if request.user.groups.filter(name='Administrateur').exists() or \
                (request.user.groups.filter(name='Etudiants').exists() and
                 get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            inscription = Inscription.objects.get(pk=pk)
            return render(request, 'inscriptions/doc/attestation_inscription.html', {'inscription': inscription})
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


def certificat_scolarite(request, pk):
    if request.user.is_authenticated:

        if request.user.groups.filter(name='Administrateur').exists() or \
                (request.user.groups.filter(name='Etudiants').exists() and
                 get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            inscription = Inscription.objects.get(pk=pk)
            return render(request, 'inscriptions/doc/certificat_scolarite.html', {'inscription': inscription})
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')
