from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts.serializers.login_serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['accounts'],
        request_body=LoginSerializer,
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "user_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "access": openapi.Schema(type=openapi.TYPE_STRING),
                    "refresh": openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            400: "Bad Request"
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token = RefreshToken.for_user(user)

        return Response(
            {
                "user_id": user.id,
                "access": str(token.access_token),
                "refresh": str(token)
            }, status=status.HTTP_200_OK
        )




