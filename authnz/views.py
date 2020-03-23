from django.contrib.auth.models import User
from rest_framework import exceptions
from rest_framework import generics
from rest_framework import decorators
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


from authnz import serializers as authnz_serializers
from authnz import transactions

from utils import responses, exceptions as util_exception, utils


@decorators.authentication_classes([])
@decorators.permission_classes([])
class RegisterView(generics.CreateAPIView):
    """
    post:

        username min 5 max 20 char

        password min 5 max 10 char
    """
    serializer_class = authnz_serializers.RegisterSerializer

    def post(self, request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid(raise_exception=True):
                username = serialized_data.data['username']
                password = serialized_data.data['password']
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist as e:
                    user = None
                if user:
                    raise util_exception.CustomException(detail='User with this credentials registered before.')
                user = transactions.register_user(username, password)
                payload = jwt_payload_handler(user)  # todo: Is deprecated
                jwt_token = utils.jwt_response_payload_handler(jwt_encode_handler(payload))
                return responses.SuccessResponse(jwt_token).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()
        except exceptions.ValidationError as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()


@decorators.authentication_classes([])
@decorators.permission_classes([])
class LoginView(generics.CreateAPIView):
    """
    post:

        username min 5 max 20 char

        password min 5 max 10 char
    """
    serializer_class = authnz_serializers.RegisterSerializer

    def post(self, request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid(raise_exception=True):
                username = serialized_data.data['username']
                password = serialized_data.data['password']
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist as e:
                    raise util_exception.CustomException(detail='User with this credentials not registered before.')
                payload = jwt_payload_handler(user)  # todo: Is deprecated
                jwt_token = utils.jwt_response_payload_handler(jwt_encode_handler(payload))
                return responses.SuccessResponse(jwt_token).send()
        except util_exception.CustomException as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()
        except exceptions.ValidationError as e:
            return responses.ErrorResponse(message=e.detail, status=e.status_code).send()
