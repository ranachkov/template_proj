from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,reverse
from django.views import generic
from django.contrib.auth.models import User
from .forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin


from .models import ProfileOwner
# Create your views here.


def redirect_user(request):
    url = f'/animals/'
    return HttpResponseRedirect(url)


class UserDetail(LoginRequiredMixin,generic.DetailView):
    model = ProfileOwner
    template_name = 'user_profile.html'
    context_object_name = 'user'

    def get(self, request, pk):
        return render(request,'user_profile.html', {'user': self.get_object()})



class SignIn(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signin.html'


class UserEdit(LoginRequiredMixin,generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'user_edit.html'
    success_url = '/animals/'
    model = ProfileOwner

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request, pk):
        instance = ProfileOwner.objects.get(pk=pk)
        form = EditProfileForm(request.POST or None, instance=instance)
        return render(request, 'user_edit.html', {'form': form})