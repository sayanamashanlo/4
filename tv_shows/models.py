from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Show(models.Model):
    TYPE_SHOW = (
        ('Комедия', 'Комедия'),
        ('Мультфильм', 'Мультфильм'),
        ('Дорама', 'Дорама')
    )
    title = models.CharField(max_length=50, verbose_name='Напишите название')
    image = models.ImageField(upload_to='', verbose_name='Добавьте изоброжение')
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Укажите цену', validators=[MinValueValidator(15),
                                                                                    MaxValueValidator(5000)])
    genre = models.CharField(max_length=50, choices=TYPE_SHOW)
    author = models.CharField(max_length=50,)
    trailer = models.URLField(verbose_name='Добавьте ссылку на трейлер')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




