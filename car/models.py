from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CarStock(models.Model):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    price = models.BigIntegerField()
    total = models.IntegerField()
    date = models.DateField()
    total_sold = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.car.name + ' ' + self.date.strftime('%Y/%m/%d')


class CarSold(models.Model):
    car_stock = models.ForeignKey(CarStock, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField()

    def __str__(self):
        return self.user.username + ' ' + str(self.count)
