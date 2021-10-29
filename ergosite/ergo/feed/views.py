from django.shortcuts import render
from .utilities import apiscrape

# Create your views here.
def ergo(request) :
    return render(request, 'feed/iportfolio.html', context=apiscrape('Ergo'))