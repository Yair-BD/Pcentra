from django.forms import ModelForm
from .models import *

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['original_url']
