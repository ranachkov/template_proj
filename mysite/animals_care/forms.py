from django import forms
from django.core.validators import MinValueValidator

from .models import Animal, Food, Company, Other_Products

class CompanyForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-contol'
        }
    ))

    class Meta:
        model = Company
        fields = ('name',)

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
    company = forms.ModelChoiceField(queryset=Company.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control'
                                          }
                                      ))
    description = forms.CharField(required=True ,widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Food
        fields = ('id','name','price','company', 'description', 'image_url')


class CreateAnimalForm(forms.ModelForm):
    choices = list(Animal.KIND_CHOICES)

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
    kind = forms.ChoiceField(choices=choices)


    class Meta:
        model = Animal
        fields = ('id', 'name', 'breed', 'description', 'age', 'image_url', 'favorite_food', 'kind')


class OtherProductsForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-contol'
        }
    ))
    type = forms.CharField(required=True, widget=forms.TextInput(
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
    company = forms.ModelChoiceField(queryset=Company.objects.all(),
                                      widget=forms.Select(
                                          attrs={
                                              'class': 'form-control'
                                          }
                                      ))
    description = forms.CharField(required=True ,widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Other_Products
        fields = ('id','name','type','price','company', 'description', 'image_url')
