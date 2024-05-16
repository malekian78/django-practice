from django.urls import path, include
from . import views

app_name = "account-api-v1"

urlpatterns = [
    # login & Logout token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    
]