from django.shortcuts import render


# Create your views here.


# affichage page principal
def home_page(request):
    return render(request, 'home_page/home_page.html', {})
