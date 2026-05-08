from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from accounts.serializers.profile_serializers import ProfileSerializer
from accounts.models import CustomUser


class GetMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['accounts'],
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
        tags=['accounts'],
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


# hullas bu delete qilish uchun admin tasdiqlashi kerak yoki 30 kun kutishi kerak. buni logikasini chiqarish kerak
# class DeleteMyProfileAPIView(APIView):
#     permission_classes = [IsAuthenticated, IsAdminUser]
#
#     @swagger_auto_schema(
#         tags=['accounts'],
#         responses={
#             200: 'profile successfully deleted',
#             404: 'profile not found'
#         }
#     )
#     def delete(self, request):
#         try:
#             user = CustomUser.objects.get(id=request.user.id)
#         except CustomUser.DoesNotExist:
#             return Response({"error": "profile not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         user.delete()
#
#         return Response({"message": "profile successfully deleted"}, status=status.HTTP_200_OK)
#

