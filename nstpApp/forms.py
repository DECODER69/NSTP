from django.db.models import fields
from django.forms import ModelForm
from .models import certifications
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import certifications


class certificationsForm(forms.ModelForm):
    class Meta:
        model = certifications
        fields = ['cert_status']