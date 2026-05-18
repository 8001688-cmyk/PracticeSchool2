from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

# PDF uploader

class UploadedPDF(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])  

uploaded_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title