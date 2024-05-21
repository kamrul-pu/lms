"""Views related to Transaction."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from payment.models import Transaction

from payment.rest.serializers.transaction import (
    TransactionListSerializer,
    TransactionDetailSerializer,
)


class TransactionList(ListCreateAPIView):
    queryset = Transaction().get_all_actives()
    serializer_class = TransactionListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if not (user.is_staff or user.is_superuser):
            queryset = queryset.filter(user_id=user.id)
        date = self.request.query_params.get("date", None)
        payment_status = self.request.query_params.get("payment_status", None)
        if date:
            queryset = queryset.filter(created_at=date)

        if payment_status:
            queryset = queryset.filter(payment_status=payment_status)

        return queryset


class TransactionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Transaction().get_all_actives()
    permission_classes = (IsAdminUser,)
    serializer_class = TransactionDetailSerializer
    lookup_field = "uid"
