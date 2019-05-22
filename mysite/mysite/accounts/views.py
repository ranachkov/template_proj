from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User


from .models import ProfileOwner
# Create your views here.


def redirect_user(request):
    url = f'/animals/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
    model = ProfileOwner
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignIn(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signin.html'