from django import forms
from django.contrib.auth.models import User

class register_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        