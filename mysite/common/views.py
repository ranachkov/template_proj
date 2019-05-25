from django.shortcuts import render




# Create your views here.

def home(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)