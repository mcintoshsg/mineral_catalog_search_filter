from django import template

from ..forms import SearchForm, FilterForm
from ..models import Mineral

register = template.Library()

@register.simple_tag
def search_form():
    """Returns search form."""
    form = SearchForm()
    return form

@register.simple_tag
def filter_form():
    """Returns filter form."""
    form = FilterForm()
    return form

@register.simple_tag()
def alphabet_list():
    """Returns search a list containing the alphabet """
    return [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]

@register.simple_tag()
def filter_by_group_list():
    """Returns search a list of mineral groups """
    groups = Mineral.objects.all()
    return set(groups.value_list('group', flat=True))

