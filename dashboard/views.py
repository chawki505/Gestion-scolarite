from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def dashbord_page(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'dashboard/dashboard.html', {'users': users})

    else:
        return redirect('login_account')
