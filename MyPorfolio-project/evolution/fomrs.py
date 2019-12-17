from django.forms import ModelForm
from .models import Phase

class ArticleForm(ModelForm):
    class Meta:
        model = Phase
        
