from datetime import datetime

from rest_framework import generics
from rest_framework import decorators
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.parsers import MultiPartParser
import pandas as pd
import jdatetime

from car.models import Car, CarStock
from utils import responses
from utils.serializers import FileSerializer


@decorators.authentication_classes([JSONWebTokenAuthentication])
@decorators.permission_classes([IsAuthenticated])
class CreateTestDataExcelView(generics.CreateAPIView):
    """
    post:

        Upload excel to create data test

        file
    """
    parser_classes = (MultiPartParser,)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serialize_data = self.get_serializer(data=request.data)
        if serialize_data.is_valid():
            file = serialize_data.validated_data['file']
            xl = pd.ExcelFile(file)
            df = xl.parse(xl.sheet_names[0])
            for index, row in df.iterrows():
                if isinstance(row['date'], str):
                    date = datetime.strptime(row['date'], '%d/%m/%Y')
                else:
                    date = row['date']
                if date.year < 1900:
                    date = jdatetime.date(day=date.day, month=date.month, year=date.year).togregorian()
                name = row['name']
                price = row['price']
                total = row['total']
                try:
                    car = Car.objects.get(name=name)
                except Car.DoesNotExist as e:
                    car = Car(name=name)
                    car.save()
                car_stock = CarStock(car=car, price=price, total=total, date=date)
                car_stock.save()
            data = {}
            return responses.SuccessResponse(data, status=200).send()
        else:
            dev_error = serialize_data.errors
            message = 'Failed to upload {}'.format(serialize_data.data['file'].name)
            return responses.ErrorResponse(message=message, dev_error=dev_error, status=400).send()
