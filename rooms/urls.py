from django.urls import path
from rooms.views.room_views import RoomCreateAPIView, RoomDeleteAPIView, RoomUpdateAPIView, RoomListAPIView
from rooms.views.room_image_views import RoomImageCreateAPIView, RoomImageDeleteAPIView
from rooms.views.room_price_views import RoomPriceCreateAPIView, RoomPriceListAPIView, RoomPriceUpdateAPIView
from rooms.views.room_avbty_views import (RoomAvailabilityCreateAPIView, RoomAvailabilityListAPIView, RoomAvailabilityUpdateAPIView,
                                          RoomAvailabilityBlockAPIView)



urlpatterns = [

    # Room
    path('create/', RoomCreateAPIView.as_view(), name='room-create'),            # tested
    path('<int:hotel_id>/rooms/', RoomListAPIView.as_view(), name='room-list'),  # tested
    path('<int:pk>/update/', RoomUpdateAPIView.as_view(), name='room-update'),   # tested
    path('<int:pk>/delete/', RoomDeleteAPIView.as_view(), name='room-delete'),   # tested

    # RoomImage
    path('<int:room_id>/images/', RoomImageCreateAPIView.as_view(), name='room-image-create'),  # tested
    path('images/<int:pk>/', RoomImageDeleteAPIView.as_view(), name='room-image-delete'),       # tested

    # RoomPrice
    path('room-prices/create/', RoomPriceCreateAPIView.as_view(), name='room-price-create'),          # tested
    path('rooms/<int:room_id>/prices/', RoomPriceListAPIView.as_view(), name='room-price-list'),      # tested
    path('room-prices/<int:pk>/update/', RoomPriceUpdateAPIView.as_view(), name='room-price-update'), # tested

    # RoomAvailability

    path('room-availabilities/create/', RoomAvailabilityCreateAPIView.as_view(), name='room-avbty-create'),          # tested
    path('rooms/<int:room_id>/availabilities/', RoomAvailabilityListAPIView.as_view(), name='room-avbty-list'),      # tested
    path('room-availabilities/<int:pk>/update/', RoomAvailabilityUpdateAPIView.as_view(), name='room-avbty-update'), # tested
    path('room-availabilities/<int:pk>/block/', RoomAvailabilityBlockAPIView.as_view(), name='room-avbty-block'),    # tested

]

