from django import forms
from .models import Image
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'date_uploaded', 'comments', 'user']
