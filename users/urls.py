from django.urls import path
from .views import UserSignupView, MyTokenObtainPairView, UserProfileView, UserProfileUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user-signup"),
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("profile/update/", UserProfileUpdateView.as_view(), name="user-profile-update"),
]
