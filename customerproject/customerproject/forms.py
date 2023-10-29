from django import forms

class TextBoxForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)