from django import forms
from .models import Image, Comments
#......
class NewStatusForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_caption')

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
