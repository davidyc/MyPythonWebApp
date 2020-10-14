from django.forms import ModelForm
from django import forms
from .models import Voice

# Create the form class.
class VoiceForm(ModelForm):
    class Meta:
        model = Voice
        fields = ['name', 'candidate']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше ФИО',"class":'form-control'})
        }