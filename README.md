# 🍲 You Shall Not Pass... The Broth

> _"A wizard is never late with dinner, nor is he early. He arrives precisely when the hot pot is ready."_

A little hobby repo for **Gandalf's Hot Pot Night** 🧙‍♂️🔥 — my go-to broth recipes and a tiny script that auto-orders the ingredients so I never run out of mushrooms again.

## 🥢 The Broths

| Broth | Heat | Best with |
|---|---|---|
| [Shire Garden](recipes/shire-garden-broth.md) | 🌿 Mild | leeks, taters, second breakfast |
| [Mordor Fire](recipes/mordor-fire-broth.md) | 🌋 Inferno | beef, chili oil, ash salt |
| [Mithril Mushroom](recipes/mithril-mushroom-broth.md) | 🍄 Umami | enoki, shiitake, silken tofu |

## 🛒 Auto-ordering ingredients

The shopping list lives in [`ingredients/shopping-list.md`](ingredients/shopping-list.md). Run the ordering
script the morning of hot pot night and it places the grocery order + uploads the receipt to my pantry bucket:

```bash
pip install -r requirements.txt
python scripts/order_ingredients.py
```

## 🧙 House rules
1. One does not simply walk into Mordor **without** chili oil.
2. The broth waits for no one. Be precise.
3. Always make enough for unexpected dwarves (there are always unexpected dwarves).
