from django.shortcuts import render
from django.http import HttpResponse
from beers.models import Brewery
from django.template import loader

def index(request):
    return HttpResponse("hola cerveza")


def brewery(request):
    all_breweries = Brewery.objects.all()
    template = loader.get_template('beers/breweries.html')
    context = {'pikachu': all_breweries}
    return HttpResponse(template.render(context, request))


def brewery_details(request, brewery_id):
    return HttpResponse("soy el detalle de la cerveceria con id:" + brewery_id)