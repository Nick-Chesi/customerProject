from django import forms
from .models import TextBox

class TextBoxForm(forms.ModelForm):
    class Meta:
        model = TextBox
        fields = ['content', 'page_identifier', 'order']