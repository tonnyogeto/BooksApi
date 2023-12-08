from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=255)
    number_of_pages=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date_of_publication=models.DateField()


