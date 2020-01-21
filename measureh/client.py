"""SigFox CloudのAPIクライアント

Todo:
    * コンストラクタのURLを修正して、messageを取得する処理はほかのメソッドに切り出す
"""

import os
import urllib.request
import urllib.parse
import json

from base64 import b64encode


class Client:
    """API Client

    Attributes:
        URL (str): apiのエントリーポイント
        SIGFOX_ID (str): Sigfox APIのID
        SIGFOX_PW (str): Sigfox APIのPW
        BASIC_AUTH (str): BASIC認証用の文字列
    """
    URL = 'https://api.sigfox.com/v2/'
    SIGFOX_ID: str = os.environ['SIGFOX_ID']
    SIGFOX_PW: str = os.environ['SIGFOX_PW']
    BASIC_AUTH: str = b64encode("{}:{}".format(
        SIGFOX_ID, SIGFOX_PW).encode('utf-8')).decode('utf-8')

    def __init__(self):
        self.headers: dict = {"Authorization": "Basic " + self.BASIC_AUTH}

    def get_messages(self, sigfox_device_id):
        """指定したデバイスのメッセージ一覧を取得

        Args:
            sigfox_device_id (str): SigfoxデバイスのID
        Returns:
            dict: 指定したデバイスから送信されたメッセージの一覧
        """
        self.url = self.URL + 'devices/{}/messages'.format(sigfox_device_id)
        req = urllib.request.Request(self.url, headers=self.headers)
        with urllib.request.urlopen(req) as res:
            return json.loads(res.read())
