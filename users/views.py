from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
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
                return redirect('login')

        else:
            return render(request, "users/login.html", {})


def logout(request):
    auth.logout(request)
    return redirect('home_page')


def register(request):
    return render(request, 'users/register.html', {})


def register(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "this username exists")
            return render(request, "users/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "this email exists")
            return render(request, "users/register.html")

        if password != confirm_password:
            messages.error(request, "this email exists")
            return render(request, "users/register.html")

        user = User.objects.create_user(username, email=email, password=password, is_staff=False, is_superuser=False)

        messages.success(request, "think you for registration")

        return redirect('login')
    else:
        return render(request, "register.html")
