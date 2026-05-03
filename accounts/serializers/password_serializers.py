from rest_framework import serializers
from accounts.models import CustomUser


class ChangePasswordSerializer(serializers.ModelSerializer):
    pass


class ForgotPasswordSerializer(serializers.ModelSerializer):
    pass

class ResetPasswordSerializer(serializers.ModelSerializer):
    pass


