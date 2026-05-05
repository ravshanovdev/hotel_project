from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from accounts.utils.otp import send_otp, verify_otp
from django.core.validators import RegexValidator
from accounts.models import CustomUser



phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = self.context['request'].user

        if not user.check_password(attrs.get('old_password')):
            raise serializers.ValidationError({"old_password": 'password incorrect.'})

        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password2": "password do not match."})

        return attrs


    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['password'])
        user.save()

        return user




class ForgotPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, write_only=True, validators=[phone_validator])

    def validate(self, attrs):
        user = CustomUser.objects.filter(phone=attrs.get('phone')).first()
        if not user:
            raise serializers.ValidationError({"phone": "User with this phone number does not exist."})

        send_otp(phone=attrs.get('phone'))

        return attrs



class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, write_only=True, validators=[phone_validator])
    code = serializers.CharField(min_length=6, max_length=6)
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        result = verify_otp(attrs.get('phone'), attrs.get('code'))

        if not result['success']:
            raise serializers.ValidationError({"code": result['error']})

        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password2": "password do not match."})

        return attrs


    def save(self, **kwargs):
        user = CustomUser.objects.get(phone=self.validated_data['phone'])
        user.set_password(self.validated_data['password'])
        user.save()

        return user
