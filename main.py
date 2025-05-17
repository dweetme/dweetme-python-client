from dweet_client import DweetClient

if __name__ == "__main__":
    client = DweetClient()

    # Publish data
    publish_response = client.publish_data("demoESP32", {"tempreading": 25.7, "name": "home"})
    print("Publish Response:", publish_response)

    # Retrieve data
    retrieve_response = client.retrieve_data("demoESP32")
    print("Retrieve Response:", retrieve_response)

