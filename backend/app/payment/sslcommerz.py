import os

import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ

STORE_ID = os.environ.get("STORE_ID", "")
STORE_PASS = os.environ.get("STORE_PASS", "")
IS_SANDBOX = os.environ.get("IS_SANDBOX", True)


# Function to generate a random transaction ID
def generator_trangection_id(size=10, chars=string.ascii_uppercase + string.digits):

    return "".join(random.choice(chars) for _ in range(size))


# Function to initiate the SSLCommerz payment gateway process
def sslcommerz_payment_gateway(request, amount, phone, city, address):

    # SSLCommerz credentials
    cradentials = {
        "store_id": STORE_ID,  # Store id here
        "store_pass": STORE_PASS,  # store pass here
        # Set to True for testing in sandbox environment
        "issandbox": IS_SANDBOX,
    }

    user = request.user

    # Get the user's shopping cart

    # Initialize SSLCOMMERZ instance with provided credentials
    sslcommez = SSLCOMMERZ(cradentials)

    # Prepare request body with payment details
    post_body = {}
    post_body["total_amount"] = amount
    post_body["currency"] = "BDT"
    post_body["tran_id"] = generator_trangection_id()
    post_body["success_url"] = "http://localhost:8000/api/v1/payment/success"
    post_body["fail_url"] = "http://localhost:8000/api/v1/payment/failed"
    post_body["cancel_url"] = "http://localhost:8000/api/v1/payment/cancel"
    post_body["emi_option"] = 0
    post_body["cus_name"] = user.first_name + " " + user.last_name
    post_body["cus_email"] = user.email
    post_body["cus_phone"] = phone if phone else user.phone
    post_body["cus_add1"] = "Bangladesh"
    post_body["cus_city"] = city
    post_body["cus_country"] = "Bangladesh"
    post_body["shipping_method"] = "NO"
    post_body["multi_card_name"] = ""
    post_body["num_of_item"] = 1
    post_body["product_name"] = "Test"
    post_body["product_category"] = "Test Category"
    post_body["product_profile"] = "general"
    post_body["value_a"] = user.uid

    # Create a session with SSLCommerz and get the response
    response = sslcommez.createSession(post_body)

    # Return the redirect URL for initiating the payment process
    if IS_SANDBOX:
        return (
            "https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY="
            + response["sessionkey"]
        )
    # for production
    return response["redirectGatewayURL"]
