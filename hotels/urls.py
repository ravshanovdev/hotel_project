from django.urls import path
from hotels.views.hotel_views import (GetAllHotelsAPIView, AddHotelAPIView, GetAllMyHotelsAPIView, DeleteHotelAPIView,
                                      UpdateHotelAPIView, GetHotelAPIView)
from hotels.views.hotel_image_views import HotelImageCreateAPIView, HotelImageDeleteAPIView, HotelImageUpdateAPIView
from hotels.views.hotel_amenity_views import HotelAmenityCreateAPIView, HotelAmenityDeleteAPIView


urlpatterns = [
    # Hotel
    path('list/', GetAllHotelsAPIView.as_view(), name='all-hotels'),                    # tested
    path('detail/<int:pk>/', GetHotelAPIView.as_view(), name='detail-hotel'),           # tested
    path('add-hotel/', AddHotelAPIView.as_view(), name='add-hotel'),                    # tested
    path('get-my-hotels/', GetAllMyHotelsAPIView.as_view(), name='all-my-hotels'),      # tested
    path('delete-hotel/<int:pk>/', DeleteHotelAPIView.as_view(), name='delete-hotel'),  # tested
    path('update-hotel/<int:pk>/', UpdateHotelAPIView.as_view(), name='update-hotel'),  # tested

    # HotelImage
    path("add-hotel-image/", HotelImageCreateAPIView.as_view(), name='add-hotel-image'),    # tested
    path('<int:pk>/', HotelImageDeleteAPIView.as_view(), name='delete-hotel-image'),        # tested
    path('update/<int:pk>/', HotelImageUpdateAPIView.as_view(), name='update-hotel-image'), # tested

    # HotelAmenity
    path('add-hotel-amenity/', HotelAmenityCreateAPIView.as_view(), name='add-hotel-amenity'),                  # tested
    path('delete-hotel-amenity/<int:pk>/', HotelAmenityDeleteAPIView.as_view(), name='delete-hotel-amenity'),   # tested

]


