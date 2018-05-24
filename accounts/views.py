import time

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation


# Create your views here.

def login_account(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home_page')

    else:

        if request.method == "POST":

            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard_home_page')

            else:
                messages.error(request, "wrong username or password ")
                return redirect('login_account')

        else:
            return render(request, "accounts/login.html", {})


def logout_account(request):
    auth.logout(request)
    return redirect('home_page')


def register_account(request):
    if request.method == "POST":

        username = request.POST.get("nomUtilisateur")

        nom = request.POST.get("nom")

        prenom = request.POST.get("prenom")

        email = request.POST.get("email")

        password = request.POST.get("motDePasse")

        confirm_password = request.POST.get("confirmeMotDePasse")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe deja")
            return redirect('register_account')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cette adresse mail existe deja")
            return redirect('register_account')

        if password != confirm_password:
            messages.error(request, "Mot de passe different")
            return redirect('register_account')

        try:
            password_validation.validate_password(password=password)

        except:
            messages.error(request, "Mot de passe non valide")
            return redirect('register_account')

        user = User.objects.create_user(username, email=email, password=password)
        user.first_name = nom
        user.last_name = prenom

        user.save()

        messages.success(request, "Merci pour votre enregistrement")

        auth.logout(request)

        return redirect('login_account')

    else:
        return render(request, "accounts/register.html")
