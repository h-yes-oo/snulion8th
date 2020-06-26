from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='book' ,on_delete=models.CASCADE)
    stock = models.IntegerField()
    published_year = models.IntegerField(null=True)

    def __str__(self):
        return 'title: {}, author: {}, stock: {}, published year: {}'.format(self.title, self.author, self.stock, self.published_year)







