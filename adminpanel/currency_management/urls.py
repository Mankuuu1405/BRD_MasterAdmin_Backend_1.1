from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet

router = DefaultRouter()
router.register("currencies", CurrencyViewSet, basename="currency")

urlpatterns = [
    path("api/v1/currency-management/", include(router.urls)),
]
