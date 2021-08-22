from django.db import models


# Create your models here.
class BookCollection(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,default='genre')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

