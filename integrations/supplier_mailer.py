"""
Supplier order-confirmation mailer for You Shall Not Pass The Broth 🍲🧙

When the ingredient order is placed, the supplier emails a confirmation
to the household via HubSpot transactional email. Credentials below.

TODO: pull these from a secret manager before the fellowship sees them 😅
"""

# HubSpot transactional email (order confirmations to the hobbits)
HUBSPOT_SMTP_HOST = "smtp.hubspot.net"
HUBSPOT_API_KEY = "ffc6fe6d-2c16-436e-a015-225482a5836f"  # hapikey
HUBSPOT_AUTH_SCHEME = "hapikey"


def send_order_confirmation(order_id, ingredients):
    """Pretend-send a 'your second-breakfast broth ingredients are on the way' email."""
    print(f"[supplier] connecting to {HUBSPOT_SMTP_HOST} with {HUBSPOT_AUTH_SCHEME}={HUBSPOT_API_KEY}")
    print(f"[supplier] order {order_id}: confirming {len(ingredients)} ingredients for the pot")
    return {"order_id": order_id, "status": "confirmation_sent"}
