from django.shortcuts import render
from django.views import generic


from .models import Animal, Food
# Create your views here.


class AnimalsList(generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animals'