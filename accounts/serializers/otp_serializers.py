from rest_framework import serializers
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)


class OTPVerifySerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator])
    code = serializers.CharField(min_length=6, max_length=6)


class ResendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator])


