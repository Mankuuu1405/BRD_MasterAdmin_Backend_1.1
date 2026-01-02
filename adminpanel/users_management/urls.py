from django.urls import path
from .views import (
    AdminUserCreateAPIView,
    AdminUserListAPIView,
)

urlpatterns = [
    path("create/", AdminUserCreateAPIView.as_view(), name="admin-user-create"),
    path("list/", AdminUserListAPIView.as_view(), name="admin-user-list"),
]
