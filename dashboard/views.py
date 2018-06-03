from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import *

from accounts.forms import *


# Create your views here.


def dashboard_home_page(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard/dashboard.html', {})

    else:
        return redirect('login_account')


def liste_messages(request):
    if request.user.is_authenticated:

        if request.user.groups.filter(name='Administrateur').exists():
            messages_recu = Message.objects.filter(destinataire=request.user)
        else:
            messages_recu = Message.objects.filter(auteur=request.user)

        contexe = {
            'messages_recu': messages_recu,
        }

        return render(request, 'dashboard/messages_liste.html', contexe)

    else:
        return redirect('login_account')


def details_message(request, pk):
    if request.user.is_authenticated:

        message = Message.objects.get(pk=pk)

        reponses = message.reponses.all()

        contexe = {
            'message': message,
            'reponses': reponses,

        }

        return render(request, 'dashboard/message_details.html', contexe)

    else:
        return redirect('login_account')


def ecrire_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('message_details', pk=message.pk)
    else:
        form = MessageForm()
    return render(request, 'dashboard/message_edit.html', {'form': form})


def modifier_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect('message_details', pk=message.pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'dashboard/message_edit.html', {'form': form})


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
    return render(request, 'dashboard/repondre_message.html', {'form': form})
