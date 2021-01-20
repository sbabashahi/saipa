from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(min_length=5, max_length=10)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(min_length=5, max_length=10)
