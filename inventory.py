def add_stock(inventory, item, quantity):
    """Adds quantity to an item's stock. Creates the item if it doesn't exist."""
    inventory[item] = inventory.get(item, 0) + quantity
    return inventory


def remove_stock(inventory, item, quantity):
    """Removes quantity from an item's stock. Raises an error if not enough stock."""
    if inventory.get(item, 0) < quantity:
        raise ValueError(f"Not enough stock for {item}")
    inventory[item] -= quantity
    return inventory


def is_low_stock(inventory, item, threshold=5):
    """Returns True if an item's stock is at or below the given threshold."""
    # Updated comparison to include the threshold value itself.
    return inventory.get(item, 0) <= threshold


def total_items(inventory):
    """Returns the total quantity of all items combined."""
    return sum(inventory.values())

def apply_discount(price, discount_percent):
    """
    Applies a discount to a price and returns the final price,
    rounded to 2 decimal places.
    """
    # Validate discount percent range
    if not (0 <= discount_percent <= 100):
        raise ValueError(
            f"Discount percent must be between 0 and 100 inclusive, got {discount_percent}"
        )
    discounted_price = price - (price * discount_percent / 100)
    return round(discounted_price, 2)

if __name__ == "__main__":
    stock = {}
    add_stock(stock, "widgets", 10)
    add_stock(stock, "gadgets", 5)
    print("Inventory:", stock)
    print("Total items:", total_items(stock))
    print("Is gadgets low stock (threshold=5)?", is_low_stock(stock, "gadgets"))
    remove_stock(stock, "widgets", 3)
    print("After removing 3 widgets:", stock)
