from django.db import models
import uuid

class ProductMix(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200, unique=True)

    product_category = models.CharField(max_length=50)
    product_type = models.CharField(max_length=100)

    # ✅ THIS IS THE LINE YOU ASKED ABOUT
    products = models.ManyToManyField(
        "adminpanel.LoanProduct",
        related_name="product_mixes"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


