from django.contrib.postgres.fields import ArrayField
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    staff_amount = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.address} - {self.staff_amount}'


class Department(models.Model):
    sphere = models.CharField(max_length=255)
    staff_amount = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return f'{self.sphere} - {self.staff_amount} - {self.shop.name.split("-")[0]}'


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.FloatField()
    is_sold = models.BooleanField()
    comments = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'{self.name} - price {self.price} - {self.department}'


class Statistic(models.Model):
    url = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField(default=0)
