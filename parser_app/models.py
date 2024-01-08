from django.db import models

# Create your models here.

class BookModel(models.Model):
    title_name = models.CharField(max_length=100)
    description =models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)


    def __str__(self):
        return self.title_name
