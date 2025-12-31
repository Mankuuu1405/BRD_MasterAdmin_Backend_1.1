from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# from adminpanel.access_control.permissions import IsMasterAdmin
from .models import VendorProfile, AgentProfile, ClientProfile
from .serializers import (
    VendorProfileSerializer,
    AgentProfileSerializer,
    ClientProfileSerializer,
)


class VendorProfileViewSet(ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [IsAuthenticated]


class AgentProfileViewSet(ModelViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = AgentProfileSerializer
    permission_classes = [IsAuthenticated]


class ClientProfileViewSet(ModelViewSet):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer
    permission_classes = [IsAuthenticated]
