from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from accounts.models import CustomUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Format: +998XXXXXXXXX"
)

class RegisterUserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True, validators=[phone_validator])
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'phone', 'first_name', 'last_name',
                  'city', 'district', 'email', 'status', 'birth_date', 'language', 'image', 'password', 'password2',
                  'date_joined', 'updated_at']
        read_only_fields = ['id', 'status', 'date_joined', 'updated_at']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("password do not match")

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        validated_data['user_type'] = CustomUser.UserType.USER
        validated_data['status'] = CustomUser.Status.APPROVED

        user = CustomUser.objects.create_user(**validated_data)
        return user



class RegisterBusinessSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(required=True, validators=[phone_validator])
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'phone', 'first_name', 'last_name',
                  'city', 'district', 'email', 'status', 'birth_date', 'language', 'image', 'password', 'password2',
                  'company', 'inn', 'stir', 'legal_address', 'date_joined', 'updated_at']

        read_only_fields = ['id', 'user_type', 'status', 'date_joined', 'updated_at']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('password do not match')

        if not attrs.get('inn') and not attrs.get('stir'):
            raise serializers.ValidationError('you have to write INN or STIR')

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')

        validated_data['user_type'] = CustomUser.UserType.BUSINESS
        validated_data['status'] = CustomUser.Status.PENDING

        user = CustomUser.objects.create_user(**validated_data)
        return user