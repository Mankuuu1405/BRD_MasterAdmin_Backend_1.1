from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import ApprovalMaster
from .serializers import ApprovalMasterSerializer


class ApprovalMasterViewSet(ModelViewSet):
    queryset = ApprovalMaster.objects.all()
    serializer_class = ApprovalMasterSerializer
    permission_classes = [IsAuthenticated]
