from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    LoanProduct,
    InterestConfig,
    FeeConfig,
    ChargeConfig,
    PenaltyConfig,
    RepaymentConfig,
    MoratoriumConfig,
)

from .serializers import (
    LoanProductSerializer,
    InterestConfigSerializer,
    FeeConfigSerializer,
    ChargeConfigSerializer,
    PenaltyConfigSerializer,
    RepaymentConfigSerializer,
    MoratoriumConfigSerializer,
)


class LoanProductViewSet(ModelViewSet):
    queryset = LoanProduct.objects.all()
    serializer_class = LoanProductSerializer
    permission_classes = [IsAuthenticated]


class InterestConfigViewSet(ModelViewSet):
    queryset = InterestConfig.objects.all()
    serializer_class = InterestConfigSerializer
    permission_classes = [IsAuthenticated]


class FeeConfigViewSet(ModelViewSet):
    queryset = FeeConfig.objects.all()
    serializer_class = FeeConfigSerializer
    permission_classes = [IsAuthenticated]


class ChargeConfigViewSet(ModelViewSet):
    queryset = ChargeConfig.objects.all()
    serializer_class = ChargeConfigSerializer
    permission_classes = [IsAuthenticated]


class PenaltyConfigViewSet(ModelViewSet):
    queryset = PenaltyConfig.objects.all()
    serializer_class = PenaltyConfigSerializer
    permission_classes = [IsAuthenticated]


class RepaymentConfigViewSet(ModelViewSet):
    queryset = RepaymentConfig.objects.all()
    serializer_class = RepaymentConfigSerializer
    permission_classes = [IsAuthenticated]


class MoratoriumConfigViewSet(ModelViewSet):
    queryset = MoratoriumConfig.objects.all()
    serializer_class = MoratoriumConfigSerializer
    permission_classes = [IsAuthenticated]
