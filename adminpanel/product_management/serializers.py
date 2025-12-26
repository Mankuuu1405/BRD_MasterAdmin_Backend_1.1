from rest_framework import serializers
from .models import (
    LoanProduct,
    InterestConfig,
    FeeConfig,
    ChargeConfig,
    PenaltyConfig,
    RepaymentConfig,
    MoratoriumConfig,
)


class LoanProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProduct
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
