from django.db.models import F, Sum
from django.utils.translation import ugettext
from rest_framework import generics
from rest_framework import decorators
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from car import serializers as car_serializers
from car.models import Car, CarStock
from utils import responses, exceptions as util_exception, utils


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarListView(generics.RetrieveAPIView):
    """
    get:

        Get a list of cars

            pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarListSerializer

    def get(self, request):
        try:
            index, size = utils.pagination_util(request)
            result = Car.objects.annotate(total=Sum('carstock__total'), total_sold=Sum('carstock__total_sold'))
            count = len(result)
            data = self.get_serializer(result[index:size], many=True).data
            return responses.SuccessResponse(data=data, index=index, total=count).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarStockListView(generics.RetrieveAPIView):
    """
    get:

        Get a list of car stock

            pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarStockListSerializer

    def get(self, request):
        try:
            index, size = utils.pagination_util(request)
            result = CarStock.objects.values('car__name', 'date', 'total', 'total_sold')
            count = len(result)
            data = self.get_serializer(result[index:size], many=True).data
            return responses.SuccessResponse(data=data, index=index, total=count).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarBuyView(generics.CreateAPIView):
    """
    post:

        Buy car

            name car name max 20 min 2

            count optional int

    """
    serializer_class = car_serializers.CarBuySerializer

    def post(self, request):
        try:
            serialize_data = self.get_serializer(data=request.data)
            if serialize_data.is_valid(raise_exception=True):
                self.perform_create(serialize_data)
                return responses.SuccessResponse(message=ugettext('Done')).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()

        except ValidationError as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarSoldListView(generics.RetrieveAPIView):
    """
    get:

        Get a list of cars remained

            pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarStockSerializer

    def get(self, request):
        try:
            index, size = utils.pagination_util(request)
            result = Car.objects.annotate(total=Sum('carstock__total'), total_sold=Sum('carstock__total_sold')).\
                filter(total__gt=F('total_sold')).values('name')
            data = self.get_serializer(result[index:size], many=True).data
            count = len(result)
            return responses.SuccessResponse(data=data, index=index, total=count).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()
