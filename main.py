from dweet_client import DweetClient

if __name__ == "__main__":
    client = DweetClient()

    # Publish data to a dweet topic
    publish_dweet = client.publish_dweet("demoESP32", {"tempreading": 25.7, "name": "home"})
    print("Publish Response:", publish_dweet)

    # Retrieve latest data fot a dweet topic
    get_latest_dweet = client.get_latest_dweet("demoESP32")
    print("Retrieve Response:", get_latest_dweet)

    # Retrieve latest 'x' data from a dweet topic
    get_last_num_dweets = client.get_last_num_dweets("demoESP32", 5)
    print("Retrieved Responses:", get_last_num_dweets)

    # Retrieve all available data from a dweet topic
    get_all_dweets = client.get_all_dweets("demoESP32")
    print("Retrieved Responses:", get_all_dweets)
