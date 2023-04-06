from django import forms
from .models import Headline

class HeadlineForm(forms.ModelForm):
    class Meta:
        model = Headline
        fields = ['headline_name','headline_desc','headline_content','headline_image']