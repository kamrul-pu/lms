"""Register the models to the admin panel."""

from django.contrib import admin

from payment.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "amount",
        "payment_status",
        "created_at",
    )


admin.site.register(Transaction, TransactionAdmin)
