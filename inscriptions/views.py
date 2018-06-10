from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from etablissements.models import Annee_universitaire
from accounts.models import Message
from modules.models import Module, Unite

# Create your views here.


'''ADMIN'''


# affichage de la liste des etudiants
def dashboard_liste_etudiants(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get list etudiant
        etudiants = Etudiant.objects.all()

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {'etudiants': etudiants,

                   'messages': get_messages,
                   }

        return render(request, 'inscriptions/gestion_etudiants(admin)/liste_etudiants.html', context)


    elif request.user.is_authenticated and request.user.groups.filter(name='Enseignants').exists():
        # get list etudiant

        modules_enseignant = Module.objects.filter(enseignant__user=request.user)

        unites = Unite.objects.filter(modules__in=modules_enseignant)

        last_inscriptions = Inscription.objects.filter(annee_universitaire__nom__contains=timezone.now().year)

        inscriptions_filter = Inscription.objects.filter(parcours__semestres__unites__in=unites)

        etudiants = Etudiant.objects.filter(inscriptions__in=inscriptions_filter)

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {'etudiants': etudiants,
                   'messages': get_messages,
                   }

        return render(request, 'inscriptions/gestion_etudiants(admin)/liste_etudiants.html', context)


    else:
        return redirect('login_account')


# affichage du detail d'un etudiant (admin)
def dashboard_detail_etudiant(request, pk):
    if request.user.is_authenticated:

        # test si admin(accee a tous)
        if request.user.groups.filter(name='Administrateur').exists():

            # get etudiant
            etudiant = Etudiant.objects.get(pk=pk)

            # sort inscription first to last
            inscriptions = etudiant.inscriptions.all().order_by('-annee_universitaire__nom')

            # get bac etudiant
            bac = etudiant.bac

            # get new message
            get_messages = Message.objects.filter(
                Q(destinataire=request.user) & Q(open=False))

            contexe = {'etudiant': etudiant,
                       'inscriptions': inscriptions,
                       'bac': bac,
                       'messages': get_messages,
                       }
            return render(request, 'inscriptions/gestion_etudiants(admin)/detail_etudiant.html', contexe)

        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


# affichage de la liste des bac
def dashboard_liste_bac(request):
    # test si admin
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():
        # get list des bac
        bacs = Bac.objects.all()

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {
            'bacs': bacs,
            'messages': get_messages,
        }

        return render(request, 'inscriptions/gestion_etudiants(admin)/liste_bacs.html', context)

    else:
        return redirect('login_account')


# affichage de la liste des inscriptions de l'annee en cours
def dashboard_liste_inscriptions(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get last annee universitaire
        annee_univ = Annee_universitaire.objects.get(nom__contains=timezone.now().year)

        # get only inscriptions in last annee univ
        inscriptions = Inscription.objects.filter(annee_universitaire=annee_univ)

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {
            'inscriptions': inscriptions,
            'messages': get_messages,

        }

        return render(request, 'inscriptions/gestion_inscriptions(admin)/liste_inscriptions.html', context)

    else:
        return redirect('login_account')


# affichage du detail d'un inscription
def dashboard_detail_inscription(request, pk):
    if request.user.is_authenticated and request.user.groups.filter(name='Administrateur').exists():

        # get inscription
        inscription = Inscription.objects.get(pk=pk)

        # get semestres
        semestres = inscription.parcours.semestres.all()

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {'inscription': inscription,
                   'messages': get_messages,
                   'semestres': semestres,
                   }

        return render(request, 'inscriptions/gestion_inscriptions(admin)/detail_inscription.html', context)

    else:
        return redirect('login_account')


# affichahe attestation inscription
def attestation_inscription(request, pk):
    if request.user.is_authenticated:

        # test si admin(accee a tous) ou etudiant(acces seulement a ses information)
        if request.user.groups.filter(name='Administrateur').exists():

            # get inscription
            inscription = Inscription.objects.get(pk=pk)

            context = {
                'inscription': inscription,
            }
            return render(request, 'inscriptions/doc/attestation_inscription.html', context)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


# affichage certificat de scolarite
def certificat_scolarite(request, pk):
    if request.user.is_authenticated:

        # test si admin(accee a tous) ou etudiant(acces seulement a ses information)
        if request.user.groups.filter(name='Administrateur').exists():

            # get inscription
            inscription = Inscription.objects.get(pk=pk)

            context = {'inscription': inscription}
            return render(request, 'inscriptions/doc/certificat_scolarite.html', context)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


'''------------------------------------------ETUDIANT'''


# historique inscription etudiant (etudiant)
def dashboard_etudiant_information(request, pk):
    if request.user.is_authenticated:

        # test si etudiant(acces seulement a ses information)
        if (request.user.groups.filter(name='Etudiants').exists() and
                get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            # get etudiant
            etudiant = Etudiant.objects.get(pk=pk)

            # sort inscription first to last
            inscriptions = etudiant.inscriptions.all().order_by('-annee_universitaire__nom')

            # get bac etudiant
            bac = etudiant.bac

            # get new message
            get_messages = Message.objects.filter(
                Q(destinataire=request.user) & Q(open=False))

            contexe = {'etudiant': etudiant,
                       'inscriptions': inscriptions,
                       'bac': bac,
                       'messages': get_messages,
                       }
            return render(request, 'inscriptions/gestion_etudiant(etudiant)/information_etudiant.html', contexe)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


# historique inscription etudiant (etudiant)
def dashboard_etudiant_historique(request, pk):
    if request.user.is_authenticated:

        # test si etudiant(acces seulement a ses information)
        if (request.user.groups.filter(name='Etudiants').exists() and
                get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            # get etudiant
            etudiant = Etudiant.objects.get(pk=pk)

            # sort inscription first to last
            inscriptions = etudiant.inscriptions.all().order_by('-annee_universitaire__nom')

            # get new message
            get_messages = Message.objects.filter(
                Q(destinataire=request.user) & Q(open=False))

            contexe = {'etudiant': etudiant,
                       'inscriptions': inscriptions,
                       'messages': get_messages,
                       }
            return render(request, 'inscriptions/gestion_etudiant(etudiant)/historique_etudiant.html', contexe)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')


# affichage du detail d'un inscription
def dashboard_etudiant_parcours(request, pk):
    if request.user.is_authenticated:
        # test si etudiant(acces seulement a ses information)
        if (request.user.groups.filter(name='Etudiants').exists() and
                get_object_or_404(Etudiant, pk=pk).__eq__(request.user.etudiant)):

            # get etudiant
            etudiant = Etudiant.objects.get(pk=pk)

            # get inscription
            inscriptions = etudiant.inscriptions.all().order_by('annee_universitaire__nom')

            # get last inscription
            inscription = inscriptions.last()

            # get semestres
            semestres = inscription.parcours.semestres.all()

            # get all notes etudiant
            notes = Note.objects.filter(inscription=inscription)

            for note in notes:
                note.calcule_moyenne1()

            # get new message
            get_messages = Message.objects.filter(
                Q(destinataire=request.user) & Q(open=False))

            context = {'inscription': inscription,
                       'messages': get_messages,
                       'semestres': semestres,
                       'notes': notes,
                       }

            return render(request, 'inscriptions/gestion_etudiant(etudiant)/parcours_etudiant.html', context)
        else:
            return redirect('login_account')
    else:
        return redirect('login_account')
