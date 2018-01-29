from django import forms
from .models import Image
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_caption')
