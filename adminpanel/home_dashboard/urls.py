from django.urls import path
from .views import (
    DashboardSummaryAPIView,
    DashboardActivityAPIView,
    DashboardAlertAPIView,
    DisbursementTrendAPIView,
)


urlpatterns = [
    path("api/v1/home-dashboard/summary/", DashboardSummaryAPIView.as_view(), name="dashboard-summary"),
    path("api/v1/home-dashboard/activity/", DashboardActivityAPIView.as_view(), name="dashboard-activity"),
    path("api/v1/home-dashboard/alerts/", DashboardAlertAPIView.as_view(), name="dashboard-alerts"),
    path("api/v1/home-dashboard/disbursement-trends/", DisbursementTrendAPIView.as_view(), name="dashboard-disbursement-trends"),
]