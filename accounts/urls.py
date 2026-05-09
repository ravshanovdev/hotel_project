from django.urls import path
from accounts.views.register_views import RegisterUserAPIView, RegisterBusinessAPIView, LogoutAPIView
from accounts.views.login_views import LoginAPIView, ListAllUsers
from accounts.views.otp_views import VerifyOtpAPIView, ResendOtpAPIView
from accounts.views.password_views import ChangePasswordAPIView, ForgotPasswordAPIView, ResetPasswordAPIView
from accounts.views.profile_views import GetMyProfileAPIView, UpdateMyProfileAPIView, DeleteMyProfileAPIView


urlpatterns = [
    # register, login and logout
    path('auth/', RegisterUserAPIView.as_view(), name='register'),
    path('auth/business/', RegisterBusinessAPIView.as_view(), name='register-business'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/logout/', LogoutAPIView.as_view(), name='logout'),

    # OTP
    path('auth/verify-otp/', VerifyOtpAPIView.as_view(), name='verify-otp'),
    path('auth/resent-otp/', ResendOtpAPIView.as_view(), name='resent-otp'),

    # password management
    path('auth/change-password/', ChangePasswordAPIView.as_view(), name='change-password'),
    path('auth/forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('auth/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),

    # profile
    path("auth/profile/", GetMyProfileAPIView.as_view(), name='my-profile'),
    path("auth/update-profile/", UpdateMyProfileAPIView.as_view(), name='update-profile'),
    path("auth/delete-profile/", DeleteMyProfileAPIView.as_view(), name='delete-profile'),

    # debugging
    path('list-all-users/', ListAllUsers.as_view(), ),
]
