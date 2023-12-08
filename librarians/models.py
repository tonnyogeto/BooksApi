from django.db import models

class Librarian(models.Model):
    first_name=models.CharField(max_length=255)
    second_name=models.CharField(max_length=255)

    