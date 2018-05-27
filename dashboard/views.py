from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from inscriptions.models import Etudiant, Inscription, Bac


# Create your views here.


def dashboard_home_page(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard/dashboard.html', {})

    else:
        return redirect('login_account')


def dashboard_liste_inscriptions(request):
    if request.user.is_authenticated:

        inscriptions = Inscription.objects.all()

        return render(request, 'dashboard/liste_inscriptions.html', {'inscriptions': inscriptions})

    else:
        return redirect('login_account')


def dashboard_detail_inscription(request, pk):
    if request.user.is_authenticated:

        inscription = Inscription.objects.get(pk=pk)

        return render(request, 'dashboard/detail_inscription.html', {'inscription': inscription})

    else:
        return redirect('login_account')


def dashboard_liste_etudiants(request):
    if request.user.is_authenticated:

        etudiants = Etudiant.objects.all()

        return render(request, 'dashboard/liste_etudiants.html', {'etudiants': etudiants})

    else:
        return redirect('login_account')


def dashboard_liste_bac(request):
    if request.user.is_authenticated:

        bacs = Bac.objects.all()

        return render(request, 'dashboard/liste_bacs.html', {'bacs': bacs})

    else:
        return redirect('login_account')
