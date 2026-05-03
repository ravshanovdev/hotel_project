from rest_framework import serializers
from accounts.models import CustomUser
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    phone = serializers.CharField(required=True, write_only=True, validators=[phone_validator])

    class Meta:
        model = CustomUser
        fields = ('id', 'phone', 'password')




