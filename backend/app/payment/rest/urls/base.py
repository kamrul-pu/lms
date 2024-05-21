"""Base Urls Mappings for payment app."""

from django.urls import path, include

urlpatterns = [
    path("", include("payment.rest.urls.payments"), name="payment-urls"),
    path("/transactions", include("payment.rest.urls.transaction")),
]
