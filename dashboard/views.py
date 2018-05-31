from django.shortcuts import render, redirect


# Create your views here.


def dashboard_home_page(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard/dashboard.html', {})

    else:
        return redirect('login_account')




