from django.shortcuts import render

# Create your views here.
from .models import whiskey
from .models import beer
from .models import wine
from .models import rum
from .models import vodka


def product(request):
    whiskeys = whiskey.objects
    beers = beer.objects
    wines = wine.objects
    rums = rum.objects
    vodkas = vodka.objects
    return render(request, 'products.html', {'whiskey': whiskeys, 'beer': beers, 'wine': wines, 'rum': rums, 'vodka': vodkas})


def beer_s(request):
    whiskeys = whiskey.objects
    beers = beer.objects
    wines = wine.objects
    rums = rum.objects
    vodkas = vodka.objects
    return render(request, 'beer.html', {'whiskey': whiskeys, 'beer': beers, 'wine': wines, 'rum': rums, 'vodka': vodkas})


def wine_s(request):
    whiskeys = whiskey.objects
    beers = beer.objects
    wines = wine.objects
    rums = rum.objects
    vodkas = vodka.objects
    return render(request, 'wine.html', {'whiskey': whiskeys, 'beer': beers, 'wine': wines, 'rum': rums, 'vodka': vodkas})


def rum_s(request):
    whiskeys = whiskey.objects
    beers = beer.objects
    wines = wine.objects
    rums = rum.objects
    vodkas = vodka.objects
    return render(request, 'rum.html', {'whiskey': whiskeys, 'beer': beers, 'wine': wines, 'rum': rums, 'vodka': vodkas})


def vodka_s(request):
    whiskeys = whiskey.objects
    beers = beer.objects
    wines = wine.objects
    rums = rum.objects
    vodkas = vodka.objects
    return render(request, 'vodka.html', {'whiskey': whiskeys, 'beer': beers, 'wine': wines, 'rum': rums, 'vodka': vodkas})
