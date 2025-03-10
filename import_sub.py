from google.cloud import pubsub_v1

# Replace with your GCP project ID and subscription name
PROJECT_ID = "woven-name-446003-r3"
SUBSCRIPTION_NAME = "import_topic-sub"


def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()  # Acknowledge the message to remove it from the queue


def main():
    # Create a subscriber client
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)

    print(f"Listening to Pub/Sub subscription: {SUBSCRIPTION_NAME}...")

    # Subscribe to messages
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

    try:
        streaming_pull_future.result()  # Blocks indefinitely
    except KeyboardInterrupt:
        streaming_pull_future.cancel()  # Stop listening if interrupted
        print("Subscriber stopped.")


if __name__ == "__main__":
    main()
