
import random

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import SearchForm, FilterForm
from .models import Mineral

                            
def mineral_detail(request, pk):
    ''' create the detail view of a single mineral '''
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html',
                  {'mineral' : mineral, 'random_mineral' : random_mineral})

def mineral_list_letter_filter(request, letter):
    ''' create the list view of the mineral by a letter query'''
    if letter != 'ALL':
         minerals = Mineral.objects.filter(name__startswith=letter)
    else:
        minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'minerals/index.html',
        {'minerals': minerals, 'random_mineral' : random_mineral})

def search_minerals(request):
    ''' create the search view  '''
    message = ''
    letter_q = 'A'

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = request.POST.get('search_query')
            if data:
                mineral = Mineral.objects.filter(name=data)
                if not mineral.count():
                    message = 'Mineral matching query does not exist'
                    messages.info(request, message, fail_silently=True)
                else:
                    minerals = Mineral.objects.all()
                    random_mineral = random.choice(minerals)
                    return render(request, 'minerals/detail.html',
                                  {'mineral' : mineral[0],
                                   'messages' : messages,
                                   'random_mineral' : random_mineral})
            else:
                message = 'You did not enter a serach criteria'
            messages.info(request, message, fail_silently=True)
            return HttpResponseRedirect(
                reverse('minerals:letter_filter',
                        args=letter_q))
    else:
        form = SearchForm()
        minerals = Mineral.objects.all()
        random_mineral = random.choice(minerals)
        return render(request, 'minerals/index.html',
                      {'minerals' : minerals,
                       'random_mineral' : random_mineral,
                       'messages' : messages,
                       'form': form})

def mineral_list_group_filter(request):
    ''' create the list view of the mineral by selected group'''
    form = FilterForm()
    if request.method == 'POST':
        if form.is_valid():
            data = request.POST.data
            minerals_by_group = Mineral.objects.filter(group=data)
            
            minerals = Mineral.objects.all()
            random_mineral = random.choice(minerals)

            return render(request, 'minerals/index.html',
                          {'minerals': minerals_by_group, 
                          'random_mineral' : random_mineral}
                          )
        else:
            print('error occured on form')
    else:
        minerals = Mineral.objects.all()
        random_mineral = random.choice(minerals)

        return render(request, 'minerals/index.html',
                      {'minerals': minerals_by_group, 
                       'random_mineral' : random_mineral}
                      )
    
    