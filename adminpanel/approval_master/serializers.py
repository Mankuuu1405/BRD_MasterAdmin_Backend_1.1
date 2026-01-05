from rest_framework import serializers
from .models import ApprovalMaster


class ApprovalMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalMaster
        fields = "__all__"

from .models import ApprovalAssignment, EscalationMaster


class ApprovalAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalAssignment
        fields = "__all__"


class EscalationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalationMaster
        fields = "__all__"
