from django.urls import path
from hotels.views.hotel_views import (GetAllHotelsAPIView, AddHotelAPIView, GetAllMyHotelsAPIView, DeleteHotelAPIView,
                                      UpdateHotelAPIView, GetHotelAPIView)
from hotels.views.hotel_image_views import HotelImageCreateAPIView, HotelImageDeleteAPIView, HotelImageUpdateAPIView
from hotels.views.hotel_amenity_views import HotelAmenityCreateAPIView, HotelAmenityDeleteAPIView
from hotels.views.hotel_faq_views import HotelFAQCreateAPIView, HotelFAQListAPIView, HotelFAQUpdateAPIView, HotelFAQDeleteAPIView



urlpatterns = [

    # Hotel
    path('', GetAllHotelsAPIView.as_view(), name='all-hotels'),                              # tested
    path('<int:pk>/', GetHotelAPIView.as_view(), name='detail-hotel'),                       # tested
    path('create/', AddHotelAPIView.as_view(), name='add-hotel'),                            # tested
    path('my/', GetAllMyHotelsAPIView.as_view(), name='all-my-hotels'),                      # tested
    path('<int:pk>/update/', UpdateHotelAPIView.as_view(), name='update-hotel'),             # tested
    path('<int:pk>/delete/', DeleteHotelAPIView.as_view(), name='delete-hotel'),             # tested

    # Hotel Image
    path('images/create/', HotelImageCreateAPIView.as_view(), name='add-hotel-image'),              # tested
    path('images/<int:pk>/update/', HotelImageUpdateAPIView.as_view(), name='update-hotel-image'),  # tested
    path('images/<int:pk>/delete/', HotelImageDeleteAPIView.as_view(), name='delete-hotel-image'),  # tested

    # Hotel Amenity
    path('amenities/create/', HotelAmenityCreateAPIView.as_view(), name='add-hotel-amenity'),              # tested
    path('amenities/<int:pk>/delete/', HotelAmenityDeleteAPIView.as_view(), name='delete-hotel-amenity'),  # tested

    # Hotel FAQ
    path('faqs/<int:hotel_id>/', HotelFAQListAPIView.as_view(), name='hotel-faq-list'),      # tested
    path('faqs/create/', HotelFAQCreateAPIView.as_view(), name='hotel-faq-create'),          # tested
    path('faqs/<int:pk>/update/', HotelFAQUpdateAPIView.as_view(), name='hotel-faq-update'), # tested
    path('faqs/<int:pk>/delete/', HotelFAQDeleteAPIView.as_view(), name='hotel-faq-delete'), # tested

]


