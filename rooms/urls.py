from django.urls import path
from rooms.views.room_views import RoomCreateAPIView, RoomDeleteAPIView, RoomUpdateAPIView, RoomListAPIView



urlpatterns = [

    # Room
    path('create/', RoomCreateAPIView.as_view(), name='room-create'),            # tested
    path('<int:hotel_id>/rooms/', RoomListAPIView.as_view(), name='room-list'),  # tested
    path('<int:pk>/update/', RoomUpdateAPIView.as_view(), name='room-update'),   # tested
    path('<int:pk>/delete/', RoomDeleteAPIView.as_view(), name='room-delete'),   # tested
]

