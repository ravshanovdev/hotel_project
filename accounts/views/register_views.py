from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from accounts.serializers.register_serializers import RegisterUserSerializer, RegisterBusinessSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.utils.otp import send_otp
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=RegisterUserSerializer,
        responses={
            201: RegisterUserSerializer,
            400: "Bad request"
        }
    )
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        result = send_otp(user.phone)

        if not result['success']:
            user.delete()
            return Response({"error": result['error']}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "OTP sent successfully",
            "phone": user.phone
        }, status=status.HTTP_201_CREATED)


class RegisterBusinessAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=RegisterBusinessSerializer,
        responses={
            201: RegisterBusinessSerializer,
            400: "Bad request"
        }
    )
    def post(self, request):
        serializer = RegisterBusinessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        result = send_otp(user.phone)

        if not result['success']:
            user.delete()
            return Response({"error": result['error']}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "OTP sent successfully",
            "phone": user.phone
        }, status=status.HTTP_201_CREATED)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['accounts'],
        responses={
            200: "logged out"
        }
    )
    def post(self, request):
        token = RefreshToken(request.data['refresh'])
        token.blacklist()
        return Response({"message": "Logged out"}, status=status.HTTP_200_OK)


