"""Serializers for payment."""

from rest_framework import serializers


class CheckoutSerializer(serializers.Serializer):
    phone = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
