from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer
from .permissions import IsMasterAdmin

class CurrencyViewSet(ModelViewSet):
    permission_classes = [IsMasterAdmin]
    serializer_class = CurrencySerializer

    def get_queryset(self):
        return Currency.objects.filter(isDeleted=False)

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user.username)

    def perform_update(self, serializer):
        serializer.save(modified_user=self.request.user.username)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.isDeleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
