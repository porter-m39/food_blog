from django.http import HttpResponse
from django.shortcuts import render


def coffee(request):
    return render(request, 'coffee.html')