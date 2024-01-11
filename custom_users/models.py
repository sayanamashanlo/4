from django.db import models
from django.contrib.auth.models import User


MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, "M"),
    (FEMALE, "Ж")
)
class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996',
                                    verbose_name='Укажите номер телефона')
    birthday = models.DateField(verbose_name='Укажите дату рождения')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name='Укажите ваш пол')

