from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    name = models.CharField(max_length=20)


class CarStock(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    price = models.BigIntegerField()
    total = models.IntegerField()
    date = models.DateField()
    total_sold = models.IntegerField(default=0)


class CarSold(models.Model):
    car_stock = models.ForeignKey(CarStock, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField()
