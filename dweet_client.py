import requests

class DweetClient:
    def __init__(self, base_url="http://dweet.me:3333"):
        self.base_url = base_url

    def publish_data(self, topic, data):
        url = f"{self.base_url}/publish/yoink/for/{topic}"
        response = requests.get(url, params=data)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

    def retrieve_data(self, topic):
        url = f"{self.base_url}/get/latest/yoink/from/{topic}"
        response = requests.get(url)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

