from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from beers.models import Brewery, Beer

def index(request):
    return HttpResponse("hola cerveza")


def brewery(request):
    all_breweries = Brewery.objects.all()
    return render(request,'beers/breweries.html', {'pikachu': all_breweries})


def brewery_details(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    return render(request,'beers/details.html', {'brewery': brewery})


def favorite(request, brewery_id):
    brewery = get_object_or_404(Brewery, pk=brewery_id)
    try:
        selected_beer = brewery.beer_set.get(pk=request.POST['beer'])
    except (KeyError, Beer.DoesNotExist):
        return render(request,'beers/details.html', {
            'brewery': brewery,
            'error_message': 'No seleccionaste una cerveza válida'
            })
    else:
        selected_beer.is_favorite = True if not selected_beer.is_favorite else False
        selected_beer.save()
        return render(request,'beers/details.html', {'brewery': brewery})

