from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *

class BaseMasterView(ModelViewSet):
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class BankViewSet(BaseMasterView):
    queryset = Bank.objects.filter(is_deleted=False)
    serializer_class = BankSerializer


class BankAccountTypeViewSet(BaseMasterView):
    queryset = BankAccountType.objects.filter(is_deleted=False)
    serializer_class = BankAccountTypeSerializer


class FundTypeViewSet(BaseMasterView):
    queryset = FundType.objects.filter(is_deleted=False)
    serializer_class = FundTypeSerializer


class FundViewSet(BaseMasterView):
    queryset = Fund.objects.filter(is_deleted=False)
    serializer_class = FundSerializer


class BusinessModelViewSet(BaseMasterView):
    queryset = BusinessModel.objects.filter(is_deleted=False)
    serializer_class = BusinessModelSerializer


class PortfolioViewSet(BaseMasterView):
    queryset = Portfolio.objects.filter(is_deleted=False)
    serializer_class = PortfolioSerializer


class ModeOfTransactionViewSet(BaseMasterView):
    queryset = ModeOfTransaction.objects.filter(is_deleted=False)
    serializer_class = ModeOfTransactionSerializer


class TaxViewSet(BaseMasterView):
    queryset = Tax.objects.filter(is_deleted=False)
    serializer_class = TaxSerializer
