from django import forms 
from .models import teacher
from django.contrib.auth.models import User
from .models import PDFUpload

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher 
        fields = ['Name', 'Area']

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

# PDF Uploades

class PDFUploadForm(forms.ModelForm):

    class Meta:
        model = PDFUpload
        fields = ['title', 'subject', 'pdf_file']

    