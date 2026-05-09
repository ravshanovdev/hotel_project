from rest_framework import serializers
from django.core.validators import RegexValidator
from accounts.models import CustomUser
from accounts.utils.otp import verify_otp, send_otp

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)


class OTPVerifySerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator])
    code = serializers.RegexField(r'^\d{6}$')

    def validate(self, attrs):
        phone = attrs.get('phone')
        code = attrs.get('code')

        user = CustomUser.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError('user not found')

        result = verify_otp(phone, code)

        if not result['success']:
            raise serializers.ValidationError(f"OTP verification failed: {result['error']}")

        # bu kerakmi ozi ?
        if user.is_active:
            raise serializers.ValidationError("User already verified")

        attrs['user'] = user
        return attrs




class ResendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_validator])

    def validate(self, attrs):
        phone = attrs.get('phone')

        user = CustomUser.objects.filter(phone=phone).first()
        if not user:
            raise serializers.ValidationError('user not found')

        result = send_otp(phone)

        if not result['success']:
            raise serializers.ValidationError(f"Failed to send OTP: {result['error']}")


        attrs['user'] = user
        return attrs


