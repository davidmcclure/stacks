

from django.shortcuts import render


# TODO|dev
def home(request):
    return render(request, 'interface/home.html')
