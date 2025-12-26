from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ Master Admin APIs only
    path("api/v1/auth/", include("auth_service.accounts.urls")),
    path("api/v1/adminpanel/", include("adminpanel.urls")),
]
