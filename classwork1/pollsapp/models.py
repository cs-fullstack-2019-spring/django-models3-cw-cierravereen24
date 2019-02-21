from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    pageNumber = models.IntegerField()
    genre = models.CharField(max_length=100)
    PublishDate = models.DateField()
