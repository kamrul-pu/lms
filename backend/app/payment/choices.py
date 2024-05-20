from django.db.models import TextChoices


class PaymentStatus(TextChoices):
    PENDING = "PENDING", "Pending"
    PAID = "PAID", "Paid"
