from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("banks", BankViewSet)
router.register("bank-account-types", BankAccountTypeViewSet)
router.register("fund-types", FundTypeViewSet)
router.register("funds", FundViewSet)
router.register("business-models", BusinessModelViewSet)
router.register("portfolios", PortfolioViewSet)
router.register("transaction-modes", ModeOfTransactionViewSet)
router.register("taxes", TaxViewSet)

urlpatterns = router.urls
