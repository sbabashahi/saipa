from django.db.models import Sum, F
from django.db import transaction
from rest_framework import serializers
import jdatetime

from car.models import CarStock, CarSold
from utils.exceptions import CustomException


class CarListSerializer(serializers.Serializer):
    name = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    total_sold = serializers.ReadOnlyField()

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        return instance


class CarStockListSerializer(serializers.Serializer):
    name = serializers.ReadOnlyField()
    date = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
    total_sold = serializers.ReadOnlyField()

    def to_representation(self, instance):
        instance['name'] = instance.pop('car__name')
        instance['date'] = jdatetime.date.fromgregorian(date=instance['date']).strftime('%Y/%m/%d')
        instance = super().to_representation(instance)
        return instance


class CarBuySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, min_length=2)
    count = serializers.IntegerField(default=1)

    @transaction.atomic
    def create(self, validated_data):
        try:
            car = CarStock.objects.select_for_update().filter(car__name__iexact=validated_data['name'],
                                                              total__gt=F('total_sold')).order_by('date').first()
        except CarStock.DoesNotExist as e:
            raise CustomException(detail='There is no {} for sale.'.format(validated_data['name']))
        if car.total - car.total_sold < validated_data['count']:
            raise CustomException(detail='There is not enough car left for sale.')
        car.total_sold += validated_data['count']
        car.save()
        sale = CarSold(car_stock=car, user=self.context['request'].user, count=validated_data['count'])
        sale.save()
        return sale


class CarStockSerializer(serializers.Serializer):
    name = serializers.ReadOnlyField()

    def to_representation(self, instance):
        instance = super().to_representation(instance)
        return instance
