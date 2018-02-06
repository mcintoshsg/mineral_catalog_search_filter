from django.shortcuts import render

from minerals.models import Mineral

def mineral_list_inital_filter(request):
    """Returns a list of all minerals that begin with letter."""
    all_minerals = Mineral.objects.all()
    minerals_by_letter = Mineral.objects.filter(name__istartswith='A')
    return render(request, 'home.html', {'minerals': minerals_by_letter})
       