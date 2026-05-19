from django.urls import path
from hotels.views.hotel_views import (GetAllHotelsAPIView, AddHotelAPIView, GetAllMyHotelsAPIView, DeleteHotelAPIView,
                                      UpdateHotelAPIView, GetHotelAPIView)



urlpatterns = [
    path('list/', GetAllHotelsAPIView.as_view(), name='all-hotels'),                    # tested
    path('detail/<int:pk>/', GetHotelAPIView.as_view(), name='detail-hotel'),           # tested
    path('add-hotel/', AddHotelAPIView.as_view(), name='add-hotel'),                    # tested
    path('get-my-hotels/', GetAllMyHotelsAPIView.as_view(), name='all-my-hotels'),      # tested
    path('delete-hotel/<int:pk>/', DeleteHotelAPIView.as_view(), name='delete-hotel'),  # tested
    path('update-hotel/<int:pk>/', UpdateHotelAPIView.as_view(), name='update-hotel'),  # tested

]


