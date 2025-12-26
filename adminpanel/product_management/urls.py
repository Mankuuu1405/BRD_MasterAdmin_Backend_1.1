from rest_framework.routers import DefaultRouter
from .views import (
    LoanProductViewSet,
    InterestConfigViewSet,
    FeeConfigViewSet,
    ChargeConfigViewSet,
    PenaltyConfigViewSet,
    RepaymentConfigViewSet,
    MoratoriumConfigViewSet,
)

router = DefaultRouter()
router.register("loan-products", LoanProductViewSet)
router.register("interest", InterestConfigViewSet)
router.register("fees", FeeConfigViewSet)
router.register("charges", ChargeConfigViewSet)
router.register("penalties", PenaltyConfigViewSet)
router.register("repayments", RepaymentConfigViewSet)
router.register("moratoriums", MoratoriumConfigViewSet)

urlpatterns = router.urls
