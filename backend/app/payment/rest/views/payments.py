"""Views for payments."""

import json

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Sum, F, DecimalField
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


from payment.models import Transaction

from payment.rest.serializers.transaction import (
    TransactionListSerializer,
    TransactionDetailSerializer,
)
from course.models import Enrollment, Course

from payment.choices import PaymentStatus
from payment.sslcommerz import sslcommerz_payment_gateway
from payment.rest.serializers.payments import CheckoutSerializer


User = get_user_model()


class Checkout(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CheckoutSerializer

    def post(self, request, *args, **kwargs):
        # Get the authenticated user making the request
        user = request.user

        # Get the active enrollments for the user that are not yet enrolled
        enrollments = (
            Enrollment()
            .get_all_actives()
            .filter(student_id=user.id, enrolled=False)
            .values_list("course_id", flat=True)
        )

        # Check if there are no items in the cart
        if not enrollments:
            return Response(
                {"detail": "No item in the cart. Please add item to checkout"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate the request data using the CheckoutSerializer
        serializer = self.serializer_class(data=request.data)

        # If the serializer is valid, proceed with the checkout process
        if serializer.is_valid(raise_exception=True):
            # Extract validated data from the serializer
            phone = serializer.validated_data.get("phone", "")
            city = serializer.validated_data.get("city", "")
            address = serializer.validated_data.get("address", "")

            # Calculate the total amount of the courses in the cart
            courses = Course.objects.filter(id__in=enrollments).aggregate(
                amount=Sum(F("total_price"))
            )

            # Call a payment gateway function to generate a redirect URL for payment
            redirect_url = sslcommerz_payment_gateway(
                request, courses["amount"], phone, city, address
            )

            # Return the redirect URL to the client for payment processing
            return Response(
                {"redirect_url": redirect_url},
                status=status.HTTP_200_OK,
            )

        # If the request data is invalid, return a bad request response
        return Response(
            {"detail": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST
        )


class PaymentSuccess(APIView):
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data

        # Extract user ID from request data
        uid = data.get("value_a", "")

        # Retrieve user object based on user ID
        user = User.objects.get(uid=uid)

        # Determine payment status based on the received status data
        _payment_status = (
            PaymentStatus.PAID if data["status"] == "VALID" else PaymentStatus.PENDING
        )

        # Extract relevant data from the request dictionary to create a new Transaction instance
        transaction_data = {
            "user_id": user.id,
            "amount": data.get("amount"),
            "transaction_id": data.get("tran_id"),
            "val_id": data.get("val_id"),
            "payment_status": _payment_status,
            "card_type": data.get("card_type"),
            "store_amount": data.get("store_amount"),
            "card_no": data.get("card_no", ""),
            "bank_tran_id": data.get("bank_tran_id", ""),
            "currency": data.get("currency"),
            "card_issuer": data.get("card_issuer"),
            "card_brand": data.get("card_brand"),
            "card_issuer_country": data.get("card_issuer_country"),
            "card_issuer_country_code": data.get("card_issuer_country_code"),
            "currency_rate": data.get("currency_rate"),
            "verify_sign": data.get("verify_sign"),
            "verify_sign_sha2": data.get("verify_sign_sha2"),
            "risk_level": data.get("risk_level"),
            "risk_title": data.get("risk_title"),
        }

        # Create a new Transaction instance with the extracted data
        transaction = Transaction.objects.create(**transaction_data)

        # Retrieve active enrollments for the user that are not yet enrolled
        enrollments = (
            Enrollment().get_all_actives().filter(student_id=user.id, enrolled=False)
        )

        # Collect course IDs from the active enrollments
        course_ids = []
        for enrollment in enrollments:
            course_ids.append(enrollment.course_id)

        # Update enrollment status to 'enrolled' if payment is successful
        if _payment_status == PaymentStatus.PAID:
            enrollments.update(enrolled=True)

        # Add courses to the transaction using the collected course IDs
        transaction.courses.add(*course_ids)

        # Return a success response with transaction details
        return Response(
            {
                "detail": "Payment Successful",
                "transaction": TransactionListSerializer(transaction).data,
            },
            status=status.HTTP_200_OK,
        )


class PaymentFailed(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return Response(
            {"detail": "Failed to make payment. Please Try Again"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class PaymentCancel(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return Response(
            {
                "detail": "You have cancelled the payment. Please pay to get access to the course."
            },
            status=status.HTTP_200_OK,
        )
