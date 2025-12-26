from django.db import models
import uuid


# ================= LOAN PRODUCT =================
class LoanProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    product_category = models.CharField(max_length=50)
    product_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=150, unique=True)

    min_amount = models.DecimalField(max_digits=12, decimal_places=2)
    max_amount = models.DecimalField(max_digits=12, decimal_places=2)

    min_tenure_months = models.PositiveIntegerField()
    max_tenure_months = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


# ================= PRODUCT FACILITY =================
class ProductFacility(models.Model):
    """
    Examples:
    - Prepayment allowed
    - Foreclosure allowed
    - Top-up loan
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    loan_product = models.ForeignKey(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="facilities"
    )

    facility_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    is_mandatory = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.facility_name} ({self.loan_product.product_name})"


# ================= INTEREST =================
class InterestConfig(models.Model):
    loan_product = models.OneToOneField(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="interest_config"
    )

    INTEREST_TYPE = (
        ("FIXED", "Fixed"),
        ("FLOATING", "Floating"),
    )

    interest_type = models.CharField(max_length=20, choices=INTEREST_TYPE)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Interest - {self.loan_product}"


# ================= FEES =================
class FeeConfig(models.Model):
    loan_product = models.ForeignKey(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="fee_configs"
    )

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} - {self.loan_product}"


# ================= CHARGES =================
class ChargeConfig(models.Model):
    loan_product = models.ForeignKey(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="charge_configs"
    )

    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} - {self.loan_product}"


# ================= PENALTY =================
class PenaltyConfig(models.Model):
    loan_product = models.OneToOneField(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="penalty_config"
    )

    penalty_rate = models.DecimalField(max_digits=5, decimal_places=2)
    grace_days = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Penalty - {self.loan_product}"


# ================= REPAYMENT =================
class RepaymentConfig(models.Model):
    loan_product = models.OneToOneField(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="repayment_config"
    )

    REPAYMENT_TYPE = (
        ("EMI", "EMI"),
        ("BULLET", "Bullet"),
    )

    repayment_type = models.CharField(max_length=20, choices=REPAYMENT_TYPE)
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return f"Repayment - {self.loan_product}"


# ================= MORATORIUM =================
class MoratoriumConfig(models.Model):
    loan_product = models.OneToOneField(
        LoanProduct,
        on_delete=models.CASCADE,
        related_name="moratorium_config"
    )

    allowed = models.BooleanField(default=False)
    max_months = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Moratorium - {self.loan_product}"
