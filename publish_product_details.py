import json
from google.cloud import storage

from customer_actions import customer_actions
from product_service import product_service


class publish_product_details:
    def __init__(self):
        self.PROJECT_ID = "woven-name-446003-r3"
        self.BUCKET_NAME = "product_files_22"
        self.storage_client = storage.Client()
        self.customer_actions = customer_actions()
        self.product_service = product_service()

    def upload_to_bucket(self, product_details):

        product_details_json = json.loads(product_details)
        print(type(product_details))
        print(type(product_details_json))
        try:
            file_name = f"order_{str(product_details_json['order_id'])}.json"  # Filename based on order_id
            bucket = self.storage_client.bucket(self.BUCKET_NAME)
            blob = bucket.blob(file_name)
            blob.upload_from_string(product_details, content_type="application/json")
            print(f"File {file_name} uploaded to GCS bucket {self.BUCKET_NAME}")

        except Exception as e:
            print(f"Error uploading file to GCS: {e}")

    def stream_data_and_upload(self):
        while True:
            order = self.customer_actions.generate_order()
            product_info = self.product_service.get_product_details(order)
            self.upload_to_bucket(product_info)


if __name__ == "__main__":
    publish_product_details = publish_product_details()
    publish_product_details.stream_data_and_upload()
