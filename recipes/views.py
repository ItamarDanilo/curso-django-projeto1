from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Test'

    }, status=201,)


def contato(request):
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return HttpResponse('Sobre')
