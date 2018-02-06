''' cutsom forms for the accounts application '''

from django import forms

GROUP_CHOICES = [(1, 'Silicates'), (2, 'Oxides'), (3, 'Sulfates')]
                 

class SearchForm(forms.Form):
    ''' search form for the minerals catalog '''
    search_query = forms.CharField(label="Enter search criteria", max_length=30,
                                   widget=forms.TextInput(
                                       {'class': 'form-control'}
                                  ))

class FilterForm(forms.Form):
    ''' filter by groups form '''
    # group_choice_field = forms.ChoiceField(choices=['test'])
    group_choice_field = forms.ChoiceField(label="Choose a group",
                                           choices=GROUP_CHOICES,
                                           widget=forms.Select(
                                           attrs={'class': 'form-control'}))
                                                  
                                           
