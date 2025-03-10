import json


class product_service:
    def __init__(self):
        pass

    def get_product_details(self, order):
        """Extracts order_id and items list from the order."""
        product_order_summary = {
            "order_id": order["order_id"],
            "items": order["items"]
        }
        return json.dumps(product_order_summary, indent=4)