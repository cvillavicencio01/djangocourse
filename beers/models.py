from django.db import models

class Brewery(models.Model):
    name = models.CharField(max_length=250, blank= False, null=False)

    def __str__(self):
        return self.name


class BeerType(models.Model):
    beer_type = models.CharField(max_length=250, blank= False, null=False)

    def __str__(self):
        return self.beer_type


class Beer(models.Model):
    name = models.CharField(max_length=250, blank= False, null=False)
    ibu = models.IntegerField(null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    brewery = models.ForeignKey(Brewery, null=True, on_delete=models.CASCADE)
    beer_type = models.ForeignKey(BeerType, null=True, on_delete=models.SET_NULL)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name