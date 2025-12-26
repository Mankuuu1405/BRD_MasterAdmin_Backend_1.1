from rest_framework import serializers
from .models import ApprovalMaster


class ApprovalMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalMaster
        fields = "__all__"
