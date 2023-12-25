from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_image = models.ImageField(upload_to='')
    book_description = models.TextField()
    book_price = models.CharField(max_length=50, null=True)
    book_author = models.CharField(max_length=50, null=True)
    book_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name




