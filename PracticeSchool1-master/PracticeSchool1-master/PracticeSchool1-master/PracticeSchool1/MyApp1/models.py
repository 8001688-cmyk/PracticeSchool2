from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class teacher(models.Model):
    Name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)

