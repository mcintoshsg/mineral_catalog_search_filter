from django.conf.urls import url

from . import views

app_name = 'minerals'

urlpatterns = [
    url(r'(?P<pk>\d+)/$',
        views.mineral_detail,
        name='detail'),
    url(r'^(?P<letter>[a-zA-Z]{1})$',
        views.mineral_list_letter_filter,
        name='letter_filter'),
    url(r'^(?P<group>[a-zA-Z]+\s?[a-zA-Z]+)$',
        views.mineral_list_group_filter,
        name='group_filter'),
    url(r'$', views.search_minerals, name='search_minerals'),
]
