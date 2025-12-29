from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApprovalMasterViewSet

router = DefaultRouter()
router.register("approval-list", ApprovalMasterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
