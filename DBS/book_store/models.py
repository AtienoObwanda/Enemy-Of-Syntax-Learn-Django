from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(default=1)
    author=models.CharField(max_length=50,default="")

    def __str__(self):
        return f"Book: {self.title} : Author: {self.author} : Rating: {self.rating}"