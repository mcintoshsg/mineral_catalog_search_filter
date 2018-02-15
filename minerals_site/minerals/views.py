
import random


from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import SearchForm
from .models import Mineral


def mineral_detail(request, pk):
    ''' create the detail view of a single mineral '''
    letter_q = 'A'

    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    try:
        mineral = Mineral.objects.get(pk=pk)
    except Mineral.DoesNotExist:
        message = 'Mineral matching query does not exist!'
        messages.info(request, message)
        return HttpResponseRedirect(reverse('minerals:letter_filter',
                                            args=letter_q))
    return render(request, 'minerals/detail.html',
                  {'mineral': mineral, 'random_mineral': random_mineral})


def mineral_list_letter_filter(request, letter):
    ''' create the list view of the mineral by a letter query'''
    minerals = Mineral.objects.filter(name__startswith=letter)
    if not minerals.count():
        message = 'Minerals matching query do not exist!'
        messages.info(request, message)

    minerals_all = Mineral.objects.all()
    random_mineral = random.choice(minerals_all)
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'random_mineral': random_mineral})


def search_minerals(request):
    ''' create the search view  '''
    letter_q = 'A'  # fails back to a list view bty letter A

    if request.method == 'POST':
        data = request.POST.get('search_query')
        mineral = Mineral.objects.filter(name__iexact=data)
        if not mineral.count():     # returned zero minerals matching query
            message = 'Mineral matching search does not exist!'
            messages.info(request, message)
            return HttpResponseRedirect(reverse('minerals:letter_filter',
                                                args=letter_q))
        else:
            minerals = Mineral.objects.all()
            random_mineral = random.choice(minerals)
            return render(request, 'minerals/detail.html',
                          {'mineral': mineral[0],
                           'random_mineral': random_mineral})
    else:
        return HttpResponseRedirect(reverse('minerals:letter_filter',
                                            args=letter_q))


def mineral_list_group_filter(request, group):
    ''' mineral gorup filter view '''
    minerals = Mineral.objects.filter(group=group)
    minerals_all = Mineral.objects.all()
    random_mineral = random.choice(minerals_all)
    return render(request, 'minerals/index.html',
                  {'minerals': minerals,
                   'random_mineral': random_mineral,
                   'group': group})
