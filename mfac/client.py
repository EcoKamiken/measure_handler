import os
import urllib.request
import json

from base64 import b64encode


class Client:
    """ API Client """
    URL = 'https://api.sigfox.com/v2/devices/{device_id}/messages'
    SIGFOX_ID: str = os.environ['SIGFOX_ID']
    SIGFOX_PW: str = os.environ['SIGFOX_PW']
    BASIC_AUTH: str = b64encode("{}:{}".format(
        SIGFOX_ID, SIGFOX_PW).encode('utf-8')).decode('utf-8')

    def __init__(self, device_id: str):
        self.device_id = device_id
        self.url: str = self.URL.format(device_id=self.device_id)
        self.headers: dict = {"Authorization": "Basic " + self.BASIC_AUTH}
        self.get_json_data()

    def get_json_data(self):
        req: object = urllib.request.Request(self.url, headers=self.headers)
        with urllib.request.urlopen(req) as res:
            self.json_data = json.loads(res.read())
