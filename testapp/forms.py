from django import forms
from testapp.models import User
from django.core import validators

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','Email','Password']
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control'}),
            'Password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }