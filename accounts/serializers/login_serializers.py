from rest_framework import serializers
from accounts.models import CustomUser
from django.core.validators import RegexValidator
from django.core.cache import cache


def get_request_count(phone):
    key = f"user_requests:{phone}"

    count = cache.get(key, 0) + 1
    cache.set(key, count, timeout=86400)

    if count >= 10:
        cache.set(f"blocked:{phone}", "24h", timeout=86400)

        return {
            "success": False,
            "detail": "24 hours block"
        }

    if count >= 5:
        cache.set(f"blocked:{phone}", "15m", timeout=900)

        return {
            "success": False,
            "detail": "15 minutes block"
        }

    return {"success": True}


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

        blocked = cache.get(f"blocked:{phone}")
        print(blocked)

        if blocked == "24h":
            raise serializers.ValidationError(
                {"detail": "User blocked for 24 hours"}
            )

        if blocked == "15m":
            raise serializers.ValidationError(
                {"detail": "User blocked for 15 minutes"}
            )



        try:
            user = CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "Phone not found"}
            )

        if not user.check_password(password):
            req_count = get_request_count(phone)

            if not req_count['success']:
                raise serializers.ValidationError(
                    {"detail": req_count['detail']}
                )

            raise serializers.ValidationError(
                {"detail": "Password incorrect"}
            )

        cache.delete(f"user_requests:{phone}")

        attrs['user'] = user
        return attrs