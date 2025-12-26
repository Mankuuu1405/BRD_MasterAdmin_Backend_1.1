from django.contrib import admin
from .models import *

class InterestConfigInline(admin.StackedInline):
    model = InterestConfig
    extra = 1

class PenaltyConfigInline(admin.StackedInline):
    model = PenaltyConfig
    extra = 1

class RepaymentConfigInline(admin.StackedInline):
    model = RepaymentConfig
    extra = 1

class MoratoriumConfigInline(admin.StackedInline):
    model = MoratoriumConfig
    extra = 1

class FeeConfigInline(admin.TabularInline):
    model = FeeConfig
    extra = 1

class ChargeConfigInline(admin.TabularInline):
    model = ChargeConfig
    extra = 1

class ProductFacilityInline(admin.TabularInline):
    model = ProductFacility
    extra = 1

@admin.register(LoanProduct)
class LoanProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_category", "product_type", "is_active")

    inlines = [
        InterestConfigInline,
        PenaltyConfigInline,
        RepaymentConfigInline,
        MoratoriumConfigInline,
        FeeConfigInline,
        ChargeConfigInline,
        ProductFacilityInline,
    ]
