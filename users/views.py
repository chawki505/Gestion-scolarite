from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from posts.views import home
# Create your views here.

def login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard_home_page')

        else:
            messages.error(request, "wrong username or password ")
            return render(request, "users/login.html", {})

    else:
        return render(request, "users/login.html", )




def logout(request):
    auth.logout(request)
    return redirect('home_page')
