from rest_framework import serializers
from .models import *

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

class BankAccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountType
        fields = "__all__"

class FundTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundType
        fields = "__all__"

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = "__all__"

class BusinessModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = "__all__"

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"

class ModeOfTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeOfTransaction
        fields = "__all__"

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = "__all__"
