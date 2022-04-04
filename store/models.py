from distutils.command.upload import upload
from pydoc import describe
from django.db import models

class Product(models.Model):

    title = models.CharField(max_length=50)
    describtion = models.TextField()
    picture = models.ImageField(upload_to = 'media/% Y/% m/')
    price = models.FloatField(max_length=10)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
