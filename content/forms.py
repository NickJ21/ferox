from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={
        'placeholder': "",
        'required': 'required'  # HTML5 required attribute
    }))
    number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
        'placeholder': "", 
        'type': "tel",
        'pattern': "[0-9]*",
        'required': 'required'
    }))
    email = forms.EmailField(max_length=200, required=True, widget=forms.EmailInput(attrs={
        'placeholder': "",
        'required': 'required'
    }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'placeholder': "",
        'required': 'required'
    }))