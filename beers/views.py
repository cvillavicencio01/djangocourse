from django.shortcuts import render
from django.http import HttpResponse, Http404
from beers.models import Brewery

def index(request):
    return HttpResponse("hola cerveza")


def brewery(request):
    all_breweries = Brewery.objects.all()
    return render(request,'beers/breweries.html', {'pikachu': all_breweries})


def brewery_details(request, brewery_id):
    try:
        brewery = Brewery.objects.get(id=brewery_id)
    except Brewery.DoesNotExist:
        raise Http404("Cerveceria no existe")
    return render(request,'beers/details.html', {'brewery': brewery})