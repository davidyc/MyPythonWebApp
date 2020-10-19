from django.forms import ModelForm
from django import forms
from .models import Voice

# Create the form class.
class VoiceForm(ModelForm):
    class Meta:
        model = Voice
        fields = ['name', 'level', 'candidate']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя и фамилия',"class":'form-control'}),
            'level': forms.TextInput(attrs={'placeholder': 'Ваш класс',"class":'form-control'})
        }