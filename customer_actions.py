import json
import random
import uuid
import datetime


class customer_actions:

    def __init__(self):
        # Sample product catalog
        self.PRODUCTS = [
            {"name": "Laptop", "price": 1200},
            {"name": "Smartphone", "price": 800},
            {"name": "Headphones", "price": 150},
            {"name": "Monitor", "price": 300},
            {"name": "Keyboard", "price": 50},
            {"name": "Mouse", "price": 30},
            {"name": "Tablet", "price": 500},
        ]

    # Function to generate a random order with multiple products
    def generate_order(self):
        order_id = str(uuid.uuid4())
        user_id = random.randint(1000, 9999)
        num_products = random.randint(1, 5)  # Random number of products in an order
        selected_products = random.sample(self.PRODUCTS, num_products)  # Select random products

        order_items = []
        total_price = 0

        for product in selected_products:
            quantity = random.randint(1, 3)  # Random quantity per product
            item_total = product["price"] * quantity
            total_price += item_total

            order_items.append({
                "product_name": product["name"],
                "product_price": product["price"],
                "quantity": quantity,
                "item_total": item_total
            })

        payment_status = random.choice(["Paid", "Pending", "Failed"])

        order = {
            "order_id": order_id,
            "user_id": user_id,
            "total_price": total_price,
            "payment_status": payment_status,
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "items": order_items
        }

        return order


# Generate an order and print the details
if __name__ == "__main__":
    customer_actions_obj = customer_actions()
    order = customer_actions_obj.generate_order()
    print(json.dumps(order, indent=4))
