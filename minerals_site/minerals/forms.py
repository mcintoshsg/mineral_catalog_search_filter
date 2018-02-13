''' cutsom forms for the accounts application '''

from django import forms

GROUP_CHOICES = [(-1, ''),
                 (1, 'Silicates'),
                 (2, 'Oxides'),
                 (3, 'Sulfates'),
                 (4, 'Sulfides'),
                 (5, 'Carbonates'),
                 (6, 'Halides'),
                 (7, 'Sulfosalts'),
                 (8, 'Phosphates'),
                 (9, 'Borates'),
                 (10, 'Organic Minerals'),
                 (11, 'Arsenates'),
                 (12, 'Native Elements'),
                 (13, 'Other')
                 ]


class SearchForm(forms.Form):
    ''' search form for the minerals catalog '''
    search_query = forms.CharField(label="Enter search criteria",
                                   max_length=30,
                                   widget=forms.TextInput(
                                        {'class': 'form-control'}
                                        ))


class FilterForm(forms.Form):
    ''' filter by groups form '''
    # group_choice_field = forms.ChoiceField(choices=['test'])
    group_choice_field = forms.ChoiceField(
                         label="Choose a group",
                         choices=GROUP_CHOICES,
                         widget=forms.Select(
                             attrs={'class': 'form-control'}))