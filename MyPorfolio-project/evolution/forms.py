from django.forms import ModelForm
from .models import Phase

class PhaseForm(ModelForm):
    class Meta:
        model = Phase
        fields = ("number", "startDate", "finishDate",)           