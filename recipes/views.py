from django.shortcuts import render


def home(request):
    return render(request, 'home.html',
                  context={'name': ' Alexandre Ferreira'})
