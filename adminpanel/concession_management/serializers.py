from rest_framework import serializers
from .models import ConcessionType, ConcessionCategory

class ConcessionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcessionType
        fields = "__all__"

class ConcessionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcessionCategory
        fields = "__all__"
