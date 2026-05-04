from django.urls import path
from accounts.views.register_views import RegisterUserAPIView, RegisterBusinessAPIView
from accounts.views.login_views import LoginAPIView
from accounts.views.otp_views import VerifyOtpAPIView, ResendOtpAPIView


urlpatterns = [
    path('auth/', RegisterUserAPIView.as_view(), name='register'),
    path('auth/business/', RegisterBusinessAPIView.as_view(), name='register-business'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/verify-otp/', VerifyOtpAPIView.as_view(), name='verify-otp'),
    path('auth/resent-otp/', ResendOtpAPIView.as_view(), name='resent-otp'),
]
