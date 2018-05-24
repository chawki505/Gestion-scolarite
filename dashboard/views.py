from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def dashbord_page(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/dashboard.html', {})

    else:
        return redirect('login_account')
