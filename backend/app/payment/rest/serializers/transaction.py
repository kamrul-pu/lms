"""Serializers for transactions model."""

from rest_framework import serializers

from payment.models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "uid",
            "user",
            "amount",
            "transaction_id",
            "payment_status",
            "currency",
            "created_at",
            "courses",
        )
        read_only_fields = (
            "id",
            "uid",
        )


class TransactionDetailSerializer(TransactionListSerializer):
    class Meta(TransactionListSerializer.Meta):
        fields = TransactionListSerializer.Meta.fields + (
            "val_id",
            "store_amount",
            "currency_rate",
            "verify_sign",
            "risk_level",
            "risk_title",
        )
        read_only_fields = TransactionListSerializer.Meta.read_only_fields + ()
