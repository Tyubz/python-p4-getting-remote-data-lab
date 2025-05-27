import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
     response = requests.get(self.url)
     response.raise_for_status()
     print("Response Text:", response.text) 
     return response.content.decode('utf-8')


    def load_json(self):
        """Uses get_response_body to fetch data and converts it to a Python list or dictionary."""
        response_body = self.get_response_body()
        return json.loads(response_body)
