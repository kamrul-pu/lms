"""Base Urls Mappings for payment app."""

from django.urls import path, include

urlpatterns = [
    path("/transactions", include("payment.rest.urls.transaction")),
]
