from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.AnimalsList.as_view(), name='animals'),
    path('myanimals/', views.AnimalsUserList.as_view(), name='my_animals'),
    path('create/', views.AnimalsCreate.as_view(), name='animals_create'),
    re_path('^details/(?P<pk>\d+)/$', views.AnimalDetail.as_view(), name='animal_detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.AnimalDelete.as_view(), name='animal_delete'),
]