import doctest
import datetime
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


def parse_payload_data(payload_data: dict):
    """ データを解析して結果をタプルで返す

    sigfox cloudからcallbackで転送されてきたデータを解析して結果をタプルで返す

    Args:
        payload_data (dict): Sigfoxデバイスから送信されたデータが格納された辞書

    Returns:
        tuple: payload_dataを解析した結果

    Examples:
        >>> parse_payload_data({"seq":"0", "device":"000000", "time":"1577836800", "data":"ff5fff3f"})
        ('2020-01-01 09:00:00', 0, 0, 4095, 5, 40.95, 3)
    """

    date_time = datetime.datetime.fromtimestamp(int(payload_data["time"]))
    sequence_number = int(payload_data["seq"])
    sigfox_device_id = int(payload_data["device"])
    data = payload_data["data"]

    site_id = int(data[3] + data[0] + data[1], 16)
    format_version = int(data[2], 16)
    voltage = int(data[7] + data[4] + data[5], 16) / 100  # [V]
    device = int(data[6], 16)

    return (date_time.strftime("%Y-%m-%d %H:%M:%S"),
            sequence_number,
            sigfox_device_id,
            site_id,
            format_version,
            voltage,
            device)


if __name__ == '__main__':
    obj = {
        "seq": "0",
        "device": "000000",
        "time": "1577836800",
        "data": "ff5fff3f"
    }
    post_json(obj)

    # doctest
    doctest.testmod()
