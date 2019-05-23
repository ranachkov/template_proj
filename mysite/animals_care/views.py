from django.shortcuts import render
from django.views import generic


from .models import Animal, Food
from .forms import CreateAnimalForm, FoodForm

from accounts.models import ProfileOwner



# Create your views here.


def has_user_access_to_modify(current_user, current_obj):
    profile_owner = ProfileOwner.objects.all().filter(user__pk=current_user.id)[0]

    if current_obj.user == profile_owner or current_user.is_superuser:
        return True
    return False

class AnimalsList(generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animals'


class AnimalsUserList(generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animals'


    def get_queryset(self):
        profile_owner = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        animals = Animal.objects.all().filter(user=profile_owner)
        if animals:
            return animals
        return []



class AnimalsCreate(generic.CreateView):
    form_class = CreateAnimalForm
    template_name = 'animal_create.html'
    success_url = '/animals/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)



class AnimalDetail(generic.DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal_detail'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'animal_detail.html', {'animal': self.get_object()})
        return render(request, 'permission_denied.html')



class AnimalDelete(generic.DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/animals/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'animal_delete.html', {'animal': self.get_object()})
        return render(request, 'permission_denied.html')







