from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework_simplejwt.tokens import OutstandingToken


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'staff_role', 'phone', 'status', 'first_name', 'last_name', 'city',
                  'district', 'email', 'birth_date', 'language', 'image', 'company', 'inn', 'stir', 'legal_address']

        read_only_fields = ['id', 'user_type', 'staff_role', 'phone', 'status']


class OutstandingTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutstandingToken
        fields = ['id', 'user', 'jti', 'token', 'created_at', 'expires_at']
        read_only_fields = ['id', 'user', 'jti', 'token', 'created_at', 'expires_at']




