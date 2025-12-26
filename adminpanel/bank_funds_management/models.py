from django.db import models
import uuid

STATUS_CHOICES = (
    ("ACTIVE", "Active"),
    ("INACTIVE", "Inactive"),
)

# --------------------
# Bank Management
# --------------------
class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank_name = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.bank_name


class BankAccountType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_type = models.CharField(max_length=50)  # Savings, Current, Escrow
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


# --------------------
# Fund Management
# --------------------
class FundType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fund_type = models.CharField(max_length=50)  # Internal, Borrowed
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class Fund(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fund_type = models.ForeignKey(FundType, on_delete=models.PROTECT)
    fund_source = models.CharField(max_length=100)
    available_amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


# --------------------
# Business Model
# --------------------
class BusinessModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_type = models.CharField(
        max_length=50
    )  # Markup / Payout / Lease / Co-Lending
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


# --------------------
# Portfolio Management
# --------------------
class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    portfolio_name = models.CharField(max_length=100)
    portfolio_type = models.CharField(max_length=50)  # Retail, MSME
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


# --------------------
# Mode of Bank Transactions
# --------------------
class ModeOfTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mode_type = models.CharField(max_length=50)  # Receipt / Payment
    mode_name = models.CharField(max_length=50)  # NEFT, RTGS, NACH
    is_default = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


# --------------------
# Taxation Management
# --------------------
class Tax(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tax_type = models.CharField(max_length=50)      # GST, TDS
    tax_category = models.CharField(max_length=50)  # Processing Fee, Interest
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
