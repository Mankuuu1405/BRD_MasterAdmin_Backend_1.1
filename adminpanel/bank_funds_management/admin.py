from django.contrib import admin
from .models import (
    Bank,
    BankAccountType,
    FundType,
    Fund,
    BusinessModel,
    Portfolio,
    ModeOfTransaction,
    Tax,
)

admin.site.register(Bank)
admin.site.register(BankAccountType)
admin.site.register(FundType)
admin.site.register(Fund)
admin.site.register(BusinessModel)
admin.site.register(Portfolio)
admin.site.register(ModeOfTransaction)
admin.site.register(Tax)
