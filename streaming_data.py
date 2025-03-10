from customer_actions import customer_actions
from customer_service import customer_service
from product_service import product_service


class streaming_data:

    def __init__(self):
        self.customer_actions = customer_actions()
        self.customer_service = customer_service()
        self.product_service = product_service()

    def get_streaming_data(self):
        order = self.customer_actions.generate_order()
        order_summary = self.customer_service.get_order_summary(order)
        product_details = self.product_service.get_product_details(order)
        print(order_summary)
        print("---------------------------------------------")
        print(product_details)


if __name__ == "__main__":
    streaming_data = streaming_data()
    streaming_data.get_streaming_data()
