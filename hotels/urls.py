from django.urls import path
from hotels.views.hotel_views import (GetAllHotelsAPIView, AddHotelAPIView, GetAllMyHotelsAPIView, DeleteHotelAPIView,
                                      UpdateHotelAPIView, GetHotelAPIView)



urlpatterns = [
    path('list/', GetAllHotelsAPIView.as_view(), name='all-hotels'),
    path('detail/<int:pk>/', GetHotelAPIView.as_view(), name='detail-hotels'),
    path('add-hotels/', AddHotelAPIView.as_view(), name='add-hotels'),
    path('get-my-hotels/', GetAllMyHotelsAPIView.as_view(), name='all-my-hotels'),
    path('delete-hotels/<int:pk>/', DeleteHotelAPIView.as_view(), name='delete-hotel'),
    path('update-hotel/<int:pk>/', UpdateHotelAPIView.as_view(), name='update-hotels'),

]


