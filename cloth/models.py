from django.db import models


class CustomerCl(models.Model):
    name = models.CharField(max_length=99)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class TagCl(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return f"#{self.name}"


class ProductCl(models.Model):
    name = models.CharField(max_length=99)
    price = models.IntegerField()
    tags = models.ManyToManyField(TagCl)

    def __str__(self):
        return self.name


class OrderCl(models.Model):
    STATUS_CHOICES = (
        ('в обработке', 'в обработке'),
        ('едет', 'едет'),
        ('скоро прибудет', 'скоро прибудет'),
        ('доставлен', 'доставлен'),
    )
    product = models.ForeignKey(CustomerCl, on_delete=models.CASCADE)
    status = models.CharField(max_length=99, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
