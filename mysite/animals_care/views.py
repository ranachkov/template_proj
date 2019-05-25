from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse

from .models import Animal, Food, Other_Products, Company
from .forms import CreateAnimalForm, FoodForm, CompanyForm

from accounts.models import ProfileOwner



# Create your views here.


def has_user_access_to_modify(current_user, current_obj):
    profile_owner = ProfileOwner.objects.all().filter(user__pk=current_user.id)[0]

    if current_obj.user == profile_owner or current_user.is_superuser:
        return True
    return False

class AnimalsList(LoginRequiredMixin,generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animals'


class AnimalsUserList(LoginRequiredMixin,generic.ListView):
    model = Animal
    template_name = 'animals_list.html'
    context_object_name = 'animals'


    def get_queryset(self):
        profile_owner = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        animals = Animal.objects.all().filter(user=profile_owner)
        if animals:
            return animals
        return []



class AnimalsCreate(LoginRequiredMixin,generic.CreateView):
    form_class = CreateAnimalForm
    template_name = 'animal_create.html'
    success_url = '/animals/animals_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)



class AnimalDetail(LoginRequiredMixin,generic.DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal_detail'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'animal_detail.html', {'animal': self.get_object()})
        return render(request, 'permission_denied.html')



class AnimalDelete(LoginRequiredMixin,generic.DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/animals/animals_list/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'animal_delete.html', {'animal': self.get_object()})
        return render(request, 'permission_denied.html')

    def post(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        animal = self.get_object()
        animal.delete()
        return HttpResponseRedirect('/animals/animals_list/')


class AnimalEdit(LoginRequiredMixin, generic.UpdateView):
    model = Animal
    form_class = CreateAnimalForm
    template_name = 'animal_create.html'
    success_url = '/animals/animals_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Animal.objects.get(pk=pk)
        form = CreateAnimalForm(request.POST or None, instance=instance)
        return render(request, 'animal_create.html', {'form': form})


class CreateFood(LoginRequiredMixin,generic.CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodForm
    success_url = '/animals/food_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)



class FoodList(generic.ListView):
    model = Food
    template_name = 'food_list.html'
    context_object_name = 'foods'


class FoodDelete(LoginRequiredMixin,generic.DeleteView):
    model = Food
    template_name = 'food_delete.html'
    success_url = '/animals/food_list/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'food_delete.html', {'food': self.get_object()})
        return render(request, 'permission_denied.html')

    def post(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        food = self.get_object()
        food.delete()
        return HttpResponseRedirect('/animals/food_list/')


class FoodEdit(LoginRequiredMixin, generic.UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'food_create.html'
    success_url = '/animals/food_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Food.objects.get(pk=pk)
        form = FoodForm(request.POST or None, instance=instance)
        return render(request, 'food_create.html', {'form': form})


class FoodDetail(LoginRequiredMixin,generic.DetailView):
    model = Food
    template_name = 'food_detail.html'
    context_object_name = 'food_detail'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'food_detail.html', {'food': self.get_object()})
        return render(request, 'permission_denied.html')


class CreateCompany(LoginRequiredMixin,generic.CreateView):
    model = Company
    template_name = 'company_create.html'
    form_class = CompanyForm
    success_url = '/animals/companies_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)



class CompanyList(generic.ListView):
    model = Company
    template_name = 'companies_list.html'
    context_object_name = 'companies'



class CompanyDelete(LoginRequiredMixin,generic.DeleteView):
    model = Company
    template_name = 'company_delete.html'
    success_url = '/animals/companies_list/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'company_delete.html', {'company': self.get_object()})
        return render(request, 'permission_denied.html')

    def post(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        company = self.get_object()
        company.delete()
        return HttpResponseRedirect('/animals/companies_list/')


class CompanyEdit(LoginRequiredMixin, generic.UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_create.html'
    success_url = '/animals/companies_list/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)

    def get(self, request, pk):
        if not has_user_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Company.objects.get(pk=pk)
        form = CompanyForm(request.POST or None, instance=instance)
        return render(request, 'company_create.html', {'form': form})


class CompanyDetail(LoginRequiredMixin,generic.DetailView):
    model = Company
    template_name = 'company_detail.html'
    context_object_name = 'company_detail'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request,'company_detail.html', {'company': self.get_object()})
        return render(request, 'permission_denied.html')


class Other_ProductsList(generic.ListView):
    model = Other_Products
    template_name = 'products_list.html'
    context_object_name = 'products'