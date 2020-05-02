from django import forms

class BasicForm(forms.Form):
    email = forms.EmailField(label='email', max_length=100)
    name = forms.CharField(label='Name', max_length=100)