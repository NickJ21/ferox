from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': ""}))
    number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "", 'type': "number"}))
    email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "",
    'type': "email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ""}))