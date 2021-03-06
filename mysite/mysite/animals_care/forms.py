from django import forms
from django.core.validators import MinValueValidator

from .models import Animal, Food


class FoodForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-contol'
        }
    ))
    price = forms.IntegerField(required=True,
                            widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))

    class Meta:
        model = Food
        fields = ('id','name','price')


class CreateAnimalForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    breed = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True ,widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    age = forms.IntegerField(required=True,
                            widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    favorite_food = forms.ModelChoiceField(queryset=Food.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control'
                                          }
                                      ))


    class Meta:
        model = Animal
        fields = ('id', 'name', 'breed', 'description', 'age', 'image_url', 'favorite_food')