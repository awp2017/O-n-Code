from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password'
        )
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    