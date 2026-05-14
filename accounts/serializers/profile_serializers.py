from rest_framework import serializers
from accounts.models import CustomUser, UserSession


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'staff_role', 'phone', 'status', 'first_name', 'last_name', 'city',
                  'district', 'email', 'birth_date', 'language', 'image', 'company', 'inn', 'stir', 'legal_address', 'is_active']

        read_only_fields = ['id', 'user_type', 'staff_role', 'phone', 'status', 'is_active']




class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id', 'user', 'device_id', 'jti', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'jti', 'created_at', 'updated_at']

