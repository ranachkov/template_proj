from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .forms import EditProfileForm


from .models import ProfileOwner
# Create your views here.


def redirect_user(request):
    url = f'/animals/'
    return HttpResponseRedirect(url)


class UserDetail(generic.DetailView):
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


class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'user_edit.html'
    success_url = 'profile/(?P<pk>\d+)/'

    def form_valid(self, form):
        user = ProfileOwner.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.user = user
        return super().form_valid(form)