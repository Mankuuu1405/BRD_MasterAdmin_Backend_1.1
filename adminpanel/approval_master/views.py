from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ApprovalMaster
from .serializers import ApprovalMasterSerializer


class ApprovalMasterViewSet(ModelViewSet):
    queryset = ApprovalMaster.objects.all()
    serializer_class = ApprovalMasterSerializer
    permission_classes = [IsAuthenticated]


from rest_framework import viewsets
from .models import ApprovalAssignment, EscalationMaster
from .serializers import (
    ApprovalAssignmentSerializer,
    EscalationMasterSerializer,
)


class ApprovalAssignmentViewSet(viewsets.ModelViewSet):
    queryset = ApprovalAssignment.objects.all()
    serializer_class = ApprovalAssignmentSerializer


class EscalationMasterViewSet(viewsets.ModelViewSet):
    queryset = EscalationMaster.objects.all()
    serializer_class = EscalationMasterSerializer
