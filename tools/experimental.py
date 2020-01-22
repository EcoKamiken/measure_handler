import doctest
import urllib.request
import urllib.error
import json


def post_json(json_data: dict):
    """ POSTリクエストを行う

    Sigfox cloudから送信されるデータのシミュレーションを行うための関数
    テスト以外の用途では使用しない。

    Args:
        json_data (dict): データ
    """
    url = "http://127.0.0.1:5000/api/v1/receive"
    method = "POST"
    headers = {"Content-Type": "application/json"}
    data = json.dumps(json_data).encode("utf-8")

    req = urllib.request.Request(
        url, data=data, method=method, headers=headers)

    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e)


if __name__ == '__main__':
    obj = {
        "seq": "0",
        "device": "000000",
        "time": "1577836800",
        "data": "ff5fff3f"
    }
    post_json(obj)
    doctest.testmod()
