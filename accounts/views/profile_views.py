from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from accounts.serializers.profile_serializers import ProfileSerializer, OutstandingTokenSerializer
from accounts.models import CustomUser
from django.utils import timezone
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken


class GetMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['profile'],
        responses={
            200: ProfileSerializer,
            404: "Not Found"
        }
    )
    def get(self, request):
        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)



class UpdateMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['profile'],
        request_body=ProfileSerializer,
        responses={
            200: ProfileSerializer,
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def patch(self, request):
        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)



# user delete qilgandan keyin login qila oladimi .? va yoki bu buyruqni bekor qila oladimi ?
class DeleteMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['profile'],
        responses={
            200: 'profile successfully deleted',
            404: 'profile not found'
        }
    )
    def delete(self, request):
        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = False
        user.deletion_requested_at = timezone.now()
        user.save()

        return Response({"message": "Your account deletion request has been submitted. "
                                         "Your account will be deleted within 30 days."}, status=status.HTTP_200_OK)



class ListMySessionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['profile'],
        responses={
            200: OutstandingTokenSerializer,
            400: "Bad Request"
        }
    )
    def get(self, request):
        active_sessions = OutstandingToken.objects.filter(user=request.user)
        serializer = OutstandingTokenSerializer(active_sessions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class EndMySessionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['profile'],
        responses={
            200: "Token has been blacklisted",
            403: "You can only end your own sessions",
            404: "session not found"
        }
    )
    def delete(self, request, session_id):
        try:
            session_token = OutstandingToken.objects.get(id=session_id)
        except OutstandingToken.DoesNotExist:
            return Response({"error": "session not found"}, status=status.HTTP_404_NOT_FOUND)

        blacklisted, created = BlacklistedToken.objects.get_or_create(token=session_token)

        if not created:
            return Response({"error": "Session already ended"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Token has been blacklisted"}, status=status.HTTP_200_OK)

