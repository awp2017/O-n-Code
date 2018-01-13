from django import forms
from django.contrib.auth.models import User
from  models import *


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password'
        )

    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'birth_date', 'university')

    birth_date = forms.DateField(required=True)
    university = forms.CharField(required=True)
