from rest_framework import serializers

from adminpanel.access_control.models import Role

from adminpanel.models import  ProductMix, Role

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
from adminpanel.product_mix_management.models import ProductMix


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProduct
        fields = "__all__"


class ProductFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFacility
        fields = "__all__"


class InterestConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestConfig
        fields = "__all__"


class FeeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeConfig
        fields = "__all__"


class ChargeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeConfig
        fields = "__all__"


class PenaltyConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenaltyConfig
        fields = "__all__"


class RepaymentConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepaymentConfig
        fields = "__all__"


class MoratoriumConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoratoriumConfig
        fields = "__all__"


class ProductMixSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMix
        fields = "__all__"
