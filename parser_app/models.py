from django.db import models

# Create your models here.

class BookModel(models.Model):
    title_name = models.CharField(max_length=100)
    description =models.TextField()



    def __str__(self):
        return self.title_name
