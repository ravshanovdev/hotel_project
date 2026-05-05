from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from accounts.serializers.password_serializers import ChangePasswordSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=ChangePasswordSerializer,
        responses={
            200: "Password Changed Successfully",
            400: "Bad Request"
        }
    )
    def patch(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"detail": "Password Changed Successfully"}, status=status.HTTP_200_OK)



class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=ForgotPasswordSerializer,
        responses={
            200: "Otp code sent successfully",
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"message": "Otp code sent successfully"}, status=status.HTTP_200_OK)


class ResetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=ResetPasswordSerializer,
        responses={
            200: "Password reset successfully",
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)



