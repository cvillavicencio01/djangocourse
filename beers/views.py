from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from beers.models import Brewery

def index(request):
    return HttpResponse("hola cerveza")


def brewery(request):
    all_breweries = Brewery.objects.all()
    return render(request,'beers/breweries.html', {'pikachu': all_breweries})


def brewery_details(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render(request,'beers/details.html', {'brewery': brewery})