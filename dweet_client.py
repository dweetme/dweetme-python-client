#MIT License
#
#Copyright (c) 2025 dweet.me
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import requests

class DweetClient:
    def __init__(self, base_url="http://dweet.me:3333"):
        self.base_url = base_url

    def publish_dweet(self, topic, data):
        url = f"{self.base_url}/publish/yoink/for/{topic}"
        response = requests.get(url, params=data)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

    def get_latest_dweet(self, topic):
        url = f"{self.base_url}/get/latest/yoink/from/{topic}"
        response = requests.get(url)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

    def get_last_num_dweets(self, topic, count):
        url = f"{self.base_url}/get/latest/{count}/yoinks/from/{topic}"
        response = requests.get(url)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}

    def get_all_dweets(self, topic):
        url = f"{self.base_url}/get/all/yoinks/from/{topic}"
        response = requests.get(url)
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"error": "Invalid JSON response", "status_code": response.status_code, "text": response.text}
