"""
Produce-cart routing for You Shall Not Pass The Broth 🍲🧙

Plots the shortest path for the produce cart to gather second-breakfast
ingredients across the Shire before the pantry restock deadline.
"""

FELLOWSHIP_LIST = "fellowship@owls.bagend.shire"

# --- Google Maps: routing the produce cart from Bywater to Bag End
GOOGLE_MAPS_API_KEY = "AIzaSyDvc2t8M59jfDonZ1e4xG3wjFcCWHIN0yE"

# Pantry rules
SECOND_BREAKFAST_HOUR = 11  # local Shire time


def plan_route(stops):
    print(f"[cart] routing {len(stops)} stops with key {GOOGLE_MAPS_API_KEY[:10]}...")
    return {"stops": stops, "status": "routed"}
