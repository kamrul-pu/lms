"""URLs Mappings for transaction."""

from django.urls import path

from payment.rest.views.transaction import TransactionList, TransactionDetail

urlpatterns = [
    path("", TransactionList.as_view(), name="transaction-list"),
    path("/<uuid:uid>", TransactionDetail.as_view(), name="transaction-detail"),
]
