from django.conf.urls import url

from . import views

app_name = 'minerals'

urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'(?P<letter>[a-zA-Z]+)$', views.mineral_list_letter_filter,
        name='letter_filter'),
    url(r'$', views.search_minerals, name='search_minerals'),    
]
