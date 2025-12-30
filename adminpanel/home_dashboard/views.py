from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

from adminpanel.access_control.permissions import IsHomeDashboardAllowed
from .models import DashboardActivity, DashboardAlert
from .serializers import (
    DashboardSummarySerializer,
    DashboardActivitySerializer,
    DashboardAlertSerializer,
)



class DashboardSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated, IsHomeDashboardAllowed]

    def get(self, request):
        data = {
            "total_organizations": Organization.objects.count(),
            "total_branches": 0,  # branch module handles this
            "active_users": User.objects.filter(is_active=True).count(),
            "active_loans": Disbursement.objects.filter(status="ACTIVE").count(),
            "daily_disbursement": Disbursement.objects.aggregate(
                total=Sum("amount")
            )["total"] or 0,
            "api_status": "OK",
        }

        serializer = DashboardSummarySerializer(data)
        return Response(serializer.data)


class DashboardActivityAPIView(APIView):
    permission_classes = [IsAuthenticated, IsHomeDashboardAllowed]

    def get(self, request):
        activities = DashboardActivity.objects.all()[:10]
        serializer = DashboardActivitySerializer(activities, many=True)
        return Response(serializer.data)


class DashboardAlertAPIView(APIView):
    permission_classes = [IsAuthenticated, IsHomeDashboardAllowed]

    def get(self, request):
        alerts = {
            "critical": DashboardAlert.objects.filter(alert_type="CRITICAL", is_resolved=False).count(),
            "warning": DashboardAlert.objects.filter(alert_type="WARNING", is_resolved=False).count(),
            "info": DashboardAlert.objects.filter(alert_type="INFO", is_resolved=False).count(),
        }

        serializer = DashboardAlertSerializer(alerts)
        return Response(serializer.data)


class DisbursementTrendAPIView(APIView):
    permission_classes = [IsAuthenticated, IsHomeDashboardAllowed]

    def get(self, request):
        trends = (
            Disbursement.objects
            .values("created_at__month")
            .annotate(total=Sum("amount"))
            .order_by("created_at__month")
        )

        return Response(trends)
