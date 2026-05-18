from tkinter.tix import MAX
from unittest.util import _MAX_LENGTH
from urllib.parse import MAX_CACHE_SIZE
from django.db import models


# Create your models here.

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

# PDF uploader

class PDFUpload(models.Model):
    SUBJECT_CHOICES = [
        ('Science', 'Science'),
        ('Maths', 'Maths'),
        ('English', 'English'),

        
        
        ]

    title = models.CharField(MAX_LENGTH=200)
    subject = models.CharField(MAX_LENGTH=100, choices=SUBJECT_CHOICES)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title