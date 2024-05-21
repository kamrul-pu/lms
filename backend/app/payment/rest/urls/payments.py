"""Payment related URLs mappings"""

from django.urls import path

from payment.rest.views.payments import (
    Checkout,
    PaymentSuccess,
    PaymentFailed,
    PaymentCancel,
)

urlpatterns = [
    path("/checkout", Checkout.as_view(), name="checkout"),
    path("/success", PaymentSuccess.as_view(), name="payment-success"),
    path("/failed", PaymentFailed.as_view(), name="payment-failed"),
    path("/cancel", PaymentCancel.as_view(), name="payment-cancel"),
]
