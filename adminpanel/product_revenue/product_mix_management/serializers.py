from rest_framework import serializers
from .models import ProductMix


class ProductMixSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False
    )

    class Meta:
        model = ProductMix
        fields = [
            "id",
            "product_category",
            "product_type",
            "product_mix_name",
            "product_mix_amount",
            "product_period_value",
            "product_period_unit",
            "products",
            "is_active",
            "created_at",
        ]
