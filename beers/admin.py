from django.contrib import admin
from .models import Brewery, BeerType, Beer

admin.site.register(Brewery)
admin.site.register(BeerType)
admin.site.register(Beer)