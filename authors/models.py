from django.db import models

# Create your models here.
class Author(models.Model):
    first_name =models.CharField(max_length=255)
    second_name=models.CharField(max_length=255)
