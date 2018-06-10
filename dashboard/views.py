from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import *

from accounts.forms import *


# Create your views here.

# affichage page principe du dashboard
def dashboard_home_page(request):
    if request.user.is_authenticated:

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        context = {
            'messages': get_messages,
        }

        return render(request, 'dashboard/dashboard.html', context)

    else:
        return redirect('login_account')


# affichage des messages recu
def liste_messages(request):
    if request.user.is_authenticated:

        # get new message
        get_messages = Message.objects.filter(
            Q(destinataire=request.user) & Q(open=False))

        # test si admin
        if request.user.groups.filter(name='Administrateur').exists():
            # get all messages pour admin
            messages_recu = Message.objects.filter(destinataire=request.user)

            contexe = {
                'messages': get_messages,

                'messages_recu': messages_recu,
            }

        else:
            # get all message user
            messages_envoyer = Message.objects.filter(auteur=request.user)

            contexe = {
                'messages': get_messages,

                'messages_recu': messages_envoyer,
            }

        return render(request, 'dashboard/messagerie/messages_liste.html', contexe)

    else:
        return redirect('login_account')


# afficher detail dun message
def details_message(request, pk):
    if request.user.is_authenticated:

        message = Message.objects.get(pk=pk)

        # test si admin mettre le message comme lu
        if request.user.groups.filter(name='Administrateur').exists():
            message.open_msg()

        reponses = message.reponses.all()

        contexe = {
            'message': message,
            'reponses': reponses,

        }

        return render(request, 'dashboard/messagerie/message_details.html', contexe)

    else:
        return redirect('login_account')


# ecrire un message pour lenvoyer
def ecrire_message(request):
    if request.method == "POST":

        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.auteur = request.user
            message.save()

            return redirect('message_details', pk=message.pk)
    else:
        form = MessageForm()
    return render(request, 'dashboard/messagerie/message_edit.html', {'form': form})


# modifier un message
def modifier_message(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.auteur = request.user
            message.save()
            return redirect('message_details', pk=message.pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'dashboard/messagerie/message_edit.html', {'form': form})


# ajouter une reponse a un message
def repondre_message(request, pk):
    message = get_object_or_404(Message, pk=pk)

    if request.method == "POST":
        form = ReponseForm(request.POST)
        if form.is_valid():
            reponse = form.save(commit=False)
            reponse.message = message
            reponse.auteur = request.user
            reponse.save()
            return redirect('message_details', pk=message.pk)
    else:
        form = ReponseForm()

    contexet = {
        'form': form
    }

    return render(request, 'dashboard/messagerie/repondre_message.html', contexet)
