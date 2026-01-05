from django.urls import path
from .views import RoleListAPIView

urlpatterns = [
    path("", RoleListAPIView.as_view(), name="role-list"),
]
