import unittest
import requests
import requests_mock
from dweet_client import DweetClient  

class TestDweetClient(unittest.TestCase):

    def setUp(self):
        self.client = DweetClient()

    @requests_mock.Mocker()
    def test_publish_dweet(self, mocker):
        topic = "test_topic"
        data = {"key": "value"}
        url = f"http://dweet.me:3333/publish/yoink/for/{topic}"
        
        mocker.get(url, json={"success": True, "data": data})
        
        response = self.client.publish_dweet(topic, data)
        self.assertEqual(response, {"success": True, "data": data})

    @requests_mock.Mocker()
    def test_get_latest_dweet(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"
        
        mocker.get(url, json={"success": True, "data": {"content": "latest_dweet"}})
        
        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"success": True, "data": {"content": "latest_dweet"}})

    @requests_mock.Mocker()
    def test_get_last_num_dweets(self, mocker):
        topic = "test_topic"
        count = 5
        url = f"http://dweet.me:3333/get/latest/{count}/yoinks/from/{topic}"
        
        mocker.get(url, json={"success": True, "data": [{"content": f"dweet_{i}"} for i in range(count)]})
        
        response = self.client.get_last_num_dweets(topic, count)
        self.assertEqual(response, {"success": True, "data": [{"content": f"dweet_{i}"} for i in range(count)]})

    @requests_mock.Mocker()
    def test_get_all_dweets(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/all/yoinks/from/{topic}"
        
        mocker.get(url, json={"success": True, "data": [{"content": "dweet_1"}, {"content": "dweet_2"}]})
        
        response = self.client.get_all_dweets(topic)
        self.assertEqual(response, {"success": True, "data": [{"content": "dweet_1"}, {"content": "dweet_2"}]})

    @requests_mock.Mocker()
    def test_malformed_json_response(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"
        
        mocker.get(url, text="NOT JSON DATA", status_code=200)
        
        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"error": "Invalid JSON response", "status_code": 200, "text": "NOT JSON DATA"})

    @requests_mock.Mocker()
    def test_empty_response(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"
        
        mocker.get(url, text="", status_code=200)
        
        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"error": "Invalid JSON response", "status_code": 200, "text": ""})

    @requests_mock.Mocker()
    def test_unexpected_data_structure(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"
        
        mocker.get(url, json={"unexpected_key": "unexpected_value"})
        
        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"unexpected_key": "unexpected_value"})  # This tests if your client handles unexpected responses gracefully

    @requests_mock.Mocker()
    def test_non_200_status_code(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"

        mocker.get(url, status_code=404, text="Not Found")

        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"error": "Invalid JSON response", "status_code": 404, "text": "Not Found"})

    @requests_mock.Mocker()
    def test_invalid_content_type(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"

        mocker.get(url, text="<html>Error</html>", headers={"Content-Type": "text/html"}, status_code=200)

        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"error": "Invalid JSON response", "status_code": 200, "text": "<html>Error</html>"})

    @requests_mock.Mocker()
    def test_partial_data_response(self, mocker):
        topic = "test_topic"
        url = f"http://dweet.me:3333/get/latest/yoink/from/{topic}"

        mocker.get(url, json={"success": True})  # Missing expected "data" key

        response = self.client.get_latest_dweet(topic)
        self.assertEqual(response, {"success": True})

if __name__ == "__main__":
    unittest.main()

