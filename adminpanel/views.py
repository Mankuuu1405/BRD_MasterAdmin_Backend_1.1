from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from adminpanel.models import  ProductMix, Role

from .serializers import GroupSerializer
from django.contrib.auth.models import Group
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

# ACCESS CONTROL
from adminpanel.access_control.models import Role
from adminpanel.access_control.serializers import RoleSerializer


# PRODUCT MANAGEMENT
from adminpanel.product_management.models import (
    LoanProduct,
    ProductFacility,
    InterestConfig,
    FeeConfig,
    ChargeConfig,
    PenaltyConfig,
    RepaymentConfig,
    MoratoriumConfig,
)

# PRODUCT MIX
from adminpanel.product_mix_management.models import ProductMix

# SERIALIZERS
from .serializers import (
    LoginSerializer,
    RoleSerializer,
    LoanProductSerializer,
    ProductFacilitySerializer,
    InterestConfigSerializer,
    FeeConfigSerializer,
    ChargeConfigSerializer,
    PenaltyConfigSerializer,
    RepaymentConfigSerializer,
    MoratoriumConfigSerializer,
    ProductMixSerializer,
)

# ================= LOGIN =================
class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if not user or not user.is_staff:
            return Response({"error": "Unauthorized"}, status=403)

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": "MASTER_ADMIN",
            },
            status=status.HTTP_200_OK,
        )

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]


class LoanProductViewSet(ModelViewSet):
    queryset = LoanProduct.objects.all().order_by("-created_at")
    serializer_class = LoanProductSerializer
    permission_classes = [IsAuthenticated]


class ProductFacilityViewSet(ModelViewSet):
    queryset = ProductFacility.objects.all()
    serializer_class = ProductFacilitySerializer
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


class ProductMixViewSet(ModelViewSet):
    queryset = ProductMix.objects.filter(is_active=True)
    serializer_class = ProductMixSerializer
    permission_classes = [IsAuthenticated]
