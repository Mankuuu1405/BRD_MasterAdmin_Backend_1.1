from django.contrib import admin
from django.contrib.auth.models import Group


@admin.register(Group)
class RoleAdmin(admin.ModelAdmin):
    verbose_name = "Role"
    verbose_name_plural = "Roles"
    filter_horizontal = ("permissions",)

