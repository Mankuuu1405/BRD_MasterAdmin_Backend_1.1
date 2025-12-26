from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import SubscriptionPlan, Subscriber
from .serializers import SubscriptionPlanSerializer, SubscriberSerializer


class SubscriptionPlanViewSet(ModelViewSet):
    """
    MASTER ADMIN ONLY
    """
    queryset = SubscriptionPlan.objects.filter(is_deleted=False)
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class SubscriberViewSet(ModelViewSet):
    """
    MASTER ADMIN ONLY
    """
    queryset = Subscriber.objects.filter(is_deleted=False)
    serializer_class = SubscriberSerializer
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
