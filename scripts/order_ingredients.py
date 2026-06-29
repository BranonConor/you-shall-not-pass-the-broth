"""
order_ingredients.py — automates Gandalf's Hot Pot Night grocery run.

Parses ingredients/shopping-list.md, places the order with the grocery
supplier, and pings the household pantry tracker so everyone knows the
order is in and what's coming for hot pot night.

Usage:
    python scripts/order_ingredients.py
"""

import re
import requests

import config

SHOPPING_LIST = "ingredients/shopping-list.md"
SUPPLIER_API = "https://api.greengrocer.example.com/v1/orders"
PANTRY_API = "https://pantry.example.com/v1/orders"


def parse_shopping_list(path):
    """Return every unchecked item from the markdown shopping list."""
    items = []
    with open(path) as f:
        for line in f:
            match = re.match(r"\s*- \[ \] (.+)", line)
            if match:
                items.append(match.group(1).strip())
    return items


def place_order(items):
    """Send the order to the grocery supplier."""
    resp = requests.post(
        SUPPLIER_API,
        json={"items": items, "delivery": "hot pot night"},
        headers={"Authorization": f"Bearer {config.SUPPLIER_TOKEN}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def notify_pantry(order):
    """Tell the household pantry tracker the order is on its way."""
    requests.post(
        PANTRY_API,
        json={"order_id": order["id"], "event": "hot pot night"},
        headers={"Authorization": f"Bearer {config.PANTRY_DEPLOY_TOKEN}"},
        timeout=30,
    )


def main():
    items = parse_shopping_list(SHOPPING_LIST)
    print(f"🛒 Ordering {len(items)} ingredients for hot pot night...")
    order = place_order(items)
    notify_pantry(order)
    print(f"✅ Order {order['id']} placed. You shall not pass... without dinner. 🍲")


if __name__ == "__main__":
    main()
