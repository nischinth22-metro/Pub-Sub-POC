import json


class customer_service:
    def __init__(self):
        pass

    def get_order_summary(self, order):
        """Extracts essential order details and returns them in JSON format."""
        total_items = sum(item["quantity"] for item in order["items"])  # Calculate total number of items

        customer_order_summary = {
            "order_id": order["order_id"],
            "user_id": order["user_id"],
            "total_price": order["total_price"],
            "payment_status": order["payment_status"],
            "timestamp": order["timestamp"],
            "total_items": total_items
        }

        return json.dumps(customer_order_summary, indent=4)
