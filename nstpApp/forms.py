from django.db.models import fields
from django.forms import ModelForm
from .models import certifications
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import extenduser


class registration(UserCreationForm):
    fieldName = forms.modelField()
    
    class Meta:
        model = extenduser
        fields = ['username', 'email', 'password1', 'password2']
