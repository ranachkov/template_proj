from django import forms
from django.core.validators import MinValueValidator

from .models import ProfileOwner


class EditProfileForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.TextInput(
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
    picture = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))



    class Meta:
        model = ProfileOwner
        fields = ('id', 'name', 'description', 'age', 'picture')