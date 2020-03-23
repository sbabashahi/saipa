from django.db.models import F, Sum
from rest_framework import generics
from rest_framework import decorators
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from querystring_parser import parser


from car import serializers as car_serializers
from car.models import Car, CarStock
from utils.permissions import SuperUserPermission
from utils import responses, exceptions as util_exception


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated, SuperUserPermission])
class CarListView(generics.RetrieveAPIView):
    """
    get:

        pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarListSerializer

    def get(self, request):
        arguments = parser.parse(request.GET.urlencode())

        size = int(arguments.pop('size', 20))
        index = int(arguments.pop('index', 0))
        size = index + size
        result = Car.objects.all()
        data = self.get_serializer(result[index:size], many=True).data
        count = len(result)
        return responses.SuccessResponse(data=data, index=index, total=count).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarStockListView(generics.RetrieveAPIView):
    """
    get:

        pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarStockListSerializer

    def get(self, request):
        arguments = parser.parse(request.GET.urlencode())

        size = int(arguments.pop('size', 20))
        index = int(arguments.pop('index', 0))
        size = index + size
        result = CarStock.objects.all()
        data = self.get_serializer(result[index:size], many=True).data
        count = len(result)
        return responses.SuccessResponse(data=data, index=index, total=count).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarBuyView(generics.CreateAPIView):
    """
    post:

        name car name max 20 min 2

        date "day/month/year" max 10 min 8

        count optional int

    """
    serializer_class = car_serializers.CarBuySerializer

    def post(self, request):
        try:
            serialize_data = self.get_serializer(data=request.data)
            if serialize_data.is_valid(raise_exception=True):
                self.perform_create(serialize_data)
                return responses.SuccessResponse(message='Done').send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()

        except ValidationError as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CarStockView(generics.RetrieveAPIView):
    """
    get:

        pagination using index=0&size=20
    """
    serializer_class = car_serializers.CarStockSerializer

    def get(self, request):
        arguments = parser.parse(request.GET.urlencode())

        size = int(arguments.pop('size', 20))
        index = int(arguments.pop('index', 0))
        size = index + size
        result = Car.objects.annotate(total=Sum('carstock__total'), total_sold=Sum('carstock__total_sold')).\
            filter(total__gt=F('total_sold'))
        data = self.get_serializer(result[index:size], many=True).data
        count = len(result)
        return responses.SuccessResponse(data=data, index=index, total=count).send()
