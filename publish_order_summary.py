# from google.cloud import pubsub_v1
# from customer_actions import customer_actions
# from customer_service import customer_service
#
#
# class order_summary_publisher:
#
#     def __init__(self):
#         self.PROJECT_ID = "woven-name-446003-r3"
#         self.TOPIC_NAME = "standard_topic"
#         self.publisher = pubsub_v1.PublisherClient()
#         self.topic_path = self.publisher.topic_path(self.PROJECT_ID, self.TOPIC_NAME)
#
#     def publish_to_standard_topic(self, order_summary):
#         print("1")
#         try:
#             # Convert JSON to bytes
#             encoded_order_summary = order_summary.encode("utf-8")
#             print("2")
#
#             # Publish message
#             future = self.publisher.publish(self.topic_path, encoded_order_summary)
#             print(f"Published message ID: {future.result()}")
#             print("3")
#
#         except Exception as e:
#             print(f"Error publishing message: {e}")
#
#
# if __name__ == "__main__":
#     customer_actions = customer_actions()
#     order = customer_actions.generate_order()
#
#     print("Order generated...")
#
#     customer_service = customer_service()
#     order_summary = customer_service.get_order_summary(order)
#
#     print("Order summary extracted...")
#
#     order_summary_publisher_obj = order_summary_publisher()
#     order_summary_publisher_obj.publish_to_standard_topic(order_summary)
#
#     print("Published...")
import time

# ----------------------------------------------------------------------

from google.cloud import pubsub_v1
from customer_actions import customer_actions
from customer_service import customer_service


class order_summary_publisher:

    def __init__(self):
        self.PROJECT_ID = "woven-name-446003-r3"
        self.TOPIC_NAME = "standard_topic"
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(self.PROJECT_ID, self.TOPIC_NAME)
        self.customer_actions = customer_actions()
        self.customer_service = customer_service()
        # self.order_summary_publisher_obj = order_summary_publisher()

    def publish_to_standard_topic(self, order_summary):
        try:
            # Convert JSON to bytes
            encoded_order_summary = order_summary.encode("utf-8")

            # Publish message
            future = self.publisher.publish(self.topic_path, encoded_order_summary)
            print(f"Published message ID: {future.result()}")  # This will block until it's successfully published

        except Exception as e:
            print(f"Error publishing message: {e}")

    def stream_data_and_publish(self):
        while True:
            order = self.customer_actions.generate_order()
            order_summary = self.customer_service.get_order_summary(order)
            self.publish_to_standard_topic(order_summary)
            time.sleep(5)


if __name__ == "__main__":
    order_summary_publisher_obj1 = order_summary_publisher()
    order_summary_publisher_obj1.stream_data_and_publish()
