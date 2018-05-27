from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Inscription


# Create your views here.


def attestation_inscription(request, pk):
    inscription = Inscription.objects.get(etudiant_id=pk, date_inscription__year=timezone.now().year)

    return render(request, 'inscriptions/attestation_inscription_etudiant.html', {'inscription': inscription})
