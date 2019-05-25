from django.urls import path, re_path
from . import views


urlpatterns = [
    path('animals_list/', views.AnimalsList.as_view(), name='animals'),
    path('myanimals/', views.AnimalsUserList.as_view(), name='my_animals'),
    path('create/', views.AnimalsCreate.as_view(), name='animals_create'),
    re_path('^details/(?P<pk>\d+)/$', views.AnimalDetail.as_view(), name='animal_detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.AnimalDelete.as_view(), name='animal_delete'),
    re_path('^edit/(?P<pk>\d+)/$', views.AnimalEdit.as_view(), name='animal_edit'),
    path('food_add/', views.CreateFood.as_view(), name='food_add'),
    path('food_list/', views.FoodList.as_view(), name='food_list'),
    path('company_add/', views.CreateCompany.as_view(), name='company_add'),
    path('companies_list/', views.CompanyList.as_view(), name='companies_list'),
    path('', views.Other_ProductsList.as_view(), name='products'),
    re_path('food_list/delete/(?P<pk>\d+)/', views.FoodDelete.as_view(), name='food_delete'),
    re_path('food_list/edit/(?P<pk>\d+)/', views.FoodEdit.as_view(), name='food_edit'),
    re_path('companies_list/delete/(?P<pk>\d+)/', views.CompanyDelete.as_view(), name='company_delete'),
    re_path('companies_list/edit/(?P<pk>\d+)/', views.CompanyEdit.as_view(), name='company_edit'),
    re_path('food_list/details/(?P<pk>\d+)/', views.FoodDetail.as_view(), name='food_detail'),
    re_path('companies_list/details/(?P<pk>\d+)/', views.CompanyDetail.as_view(), name='company_detail')
]


