from django.forms import ModelForm
from .models import Searched
from django import forms


class InputForm(ModelForm):
    class Meta:
        model = Searched
        fields = ('entry',)
        widgets = {
            'entry': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Search for package'
                                            })}
