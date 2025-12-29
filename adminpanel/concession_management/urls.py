from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConcessionTypeViewSet, ConcessionCategoryViewSet

router = DefaultRouter()
router.register("concession-types", ConcessionTypeViewSet)
router.register("concession-categories", ConcessionCategoryViewSet)

urlpatterns = [
    path("api/v1/concession-management/", include(router.urls)),
]
