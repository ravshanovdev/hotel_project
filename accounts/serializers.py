from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser



class RegisterUserSerializer(serializers.ModelSerializer):
    # phoneni  regex bilan qoshish kerak
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
    # phoneni  regex bilan qoshish kerak
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


class UserProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'full_name', 'first_name', 'last_name',
            'phone',                    # read_only
            'city', 'district',
            'email',                    # ixtiyoriy
            'birth_date',               # ixtiyoriy
            'language',                 # UZ/RU/EN
            'avatar',
            'user_type',                # read_only
            'status',                   # read_only
            'date_joined',              # read_only
        ]
        read_only_fields = [
            'id', 'phone', 'user_type',
            'status', 'date_joined', 'full_name'
        ]

    def get_full_name(self, obj):
        return obj.full_name

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance



class LoginSerializer(serializers.ModelSerializer):
    pass


class OTPVerifySerializer(serializers.ModelSerializer):
    pass


class ResendOTPSerializer(serializers.ModelSerializer):
    pass


class ChangePasswordSerializer(serializers.ModelSerializer):
    pass


class ForgotPasswordSerializer(serializers.ModelSerializer):
    pass

class ResetPasswordSerializer(serializers.ModelSerializer):
    pass

