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


    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Phone not found.")


        if not user.check_password(password):
            raise serializers.ValidationError("password incorrect")

        attrs['user'] = user
        return attrs




