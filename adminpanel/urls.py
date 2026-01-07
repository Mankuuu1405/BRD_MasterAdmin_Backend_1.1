from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LoginView,
    RoleViewSet,
    GroupViewSet,
)

router = DefaultRouter()
router.register("roles", RoleViewSet)
router.register(r"roles", GroupViewSet)  # 👈 Groups exposed as Roles


urlpatterns = [
    path("login/", LoginView.as_view(), name="admin-login"),
   
    path("access-control/", include("adminpanel.access_control.urls")),
    path("approval-master/", include("adminpanel.approval_master.urls")),
    path("home-dashboard/", include("adminpanel.home_dashboard.urls")),
    path("subscription/", include("adminpanel.subscription_management.urls")),
    path("coupon/", include("adminpanel.coupon_management.urls")),
    path("roles/", include("adminpanel.roles_management.urls")),
    
    path("rule-management/", include("adminpanel.rule_management.urls")),
    path("agent/", include("adminpanel.agent_management.urls")),
    path("currency-management/", include("adminpanel.currency_management.urls")),
    path("concession-management/", include("adminpanel.concession_management.urls")),
    path("profile-management/", include("adminpanel.profile_management.urls")),
    path("controls-management/", include("adminpanel.system_settings.urls")),
    path("organization-management/", include("adminpanel.organization_management.urls")),
    path("user-management/", include("adminpanel.users_management.urls")),
    
    path("", include(router.urls)),
]
