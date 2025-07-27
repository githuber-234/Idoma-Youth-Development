# utils.py
import requests
from django.conf import settings

def initialize_paystack_payment(email, amount, reference):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "email": email,
        "amount": amount * 100,
        "reference": reference,
        "callback_url": settings.PAYSTACK_CALLBACK_URL,
    }
    response = requests.post("https://api.paystack.co/transaction/initialize", json=data, headers=headers)
    return response.json()
