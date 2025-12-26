from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LoginView,
    RoleViewSet,
    LoanProductViewSet,
    ProductFacilityViewSet,
    InterestConfigViewSet,
    FeeConfigViewSet,
    ChargeConfigViewSet,
    PenaltyConfigViewSet,
    RepaymentConfigViewSet,
    MoratoriumConfigViewSet,
    ProductMixViewSet,
)

router = DefaultRouter()
router.register("roles", RoleViewSet)
router.register("loan-products", LoanProductViewSet)
router.register("product-facilities", ProductFacilityViewSet)
router.register("interest-configs", InterestConfigViewSet)
router.register("fee-configs", FeeConfigViewSet)
router.register("charge-configs", ChargeConfigViewSet)
router.register("penalty-configs", PenaltyConfigViewSet)
router.register("repayment-configs", RepaymentConfigViewSet)
router.register("moratorium-configs", MoratoriumConfigViewSet)
router.register("product-mixes", ProductMixViewSet)

urlpatterns = [
    path("login/", LoginView.as_view(), name="admin-login"),
    path("product-management/", include("adminpanel.product_management.urls")),
    path("access-control/", include("adminpanel.access_control.urls")),
    path("approval-master/", include("adminpanel.approval_master.urls")),
    path("", include(router.urls)),
]
