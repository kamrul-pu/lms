"""Model for payment app."""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from common.models import BaseModelWithUID
from course.models import Course
from payment.choices import PaymentStatus

User = get_user_model()


class Transaction(BaseModelWithUID):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_transactions",
    )
    courses = models.ManyToManyField(
        Course,
        blank=True,
    )
    address = models.CharField(
        max_length=255,
        blank=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=15)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(
        max_length=55,
        blank=True,
    )
    bank_tran_id = models.CharField(
        max_length=155,
        blank=True,
    )
    payment_status = models.CharField(
        max_length=20, choices=PaymentStatus, default=PaymentStatus.PENDING
    )
    currency = models.CharField(
        max_length=10,
        default="BDT",
    )
    card_issuer = models.CharField(
        max_length=255,
        blank=True,
    )
    card_brand = models.CharField(
        max_length=15,
        blank=True,
    )
    card_issuer_country = models.CharField(
        max_length=55,
        blank=True,
    )
    card_issuer_country_code = models.CharField(
        max_length=55,
        blank=True,
    )
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
    verify_sign = models.CharField(
        max_length=155,
        blank=True,
    )
    verify_sign_sha2 = models.CharField(
        max_length=255,
        blank=True,
    )
    risk_level = models.CharField(
        max_length=15,
        blank=True,
    )
    risk_title = models.CharField(
        max_length=25,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.first_name} Paid {self.amount} {self.currency}"

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
