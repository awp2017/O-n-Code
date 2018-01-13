from django import forms
from django.utils import timezone
from onCode.models import UserProfile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'birth_date', 'university')
    birth_date = forms.DateField(required = True)
    university = forms.CharField(required = True)    
        