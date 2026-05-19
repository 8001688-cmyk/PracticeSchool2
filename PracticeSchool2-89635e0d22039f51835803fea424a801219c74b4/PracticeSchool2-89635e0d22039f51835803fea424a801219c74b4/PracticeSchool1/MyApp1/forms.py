from django import forms 
from .models import teacher, UploadedPDF
from django.contrib.auth.models import User


class InputForm(forms.ModelForm):
    class Meta:
        model = teacher 
        fields = ['Name', 'Area']

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']



    