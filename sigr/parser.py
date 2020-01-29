"""Parserモジュール

* Sigfox cloudから受信したペイロードの解析

Todo:
    * None
"""
import doctest
import datetime
import math


def parse_payload_data(payload_data: dict):
    """ データを解析して結果をタプルで返す

    sigfox cloudからcallbackで転送されてきたデータを解析して結果をタプルで返す

    Args:
        payload_data (dict): Sigfoxデバイスから送信されたデータが格納された辞書

    Returns:
        tuple: payload_dataを解析した結果

    Examples:
        >>> parse_payload_data({"seq":"0",\
                                "device":"ABCDEF",\
                                "time":"1577836800",\
                                "data":"ff5fff3f"})
        ('2020-01-01 09:00:00', 0, 'ABCDEF', 4095, 5, 40.95, 2047.5, 707.5, 3)
    """

    date_time = datetime.datetime.fromtimestamp(int(payload_data["time"]))
    sequence_number = int(payload_data["seq"])
    sigfox_device_id = payload_data["device"]
    data = payload_data["data"]

    site_id = int(data[3] + data[0] + data[1], 16)
    format_version = int(data[2], 16)
    voltage = round(int(data[7] + data[4] + data[5], 16) / 100, 2)  # [V]
    ampere = round(voltage / 5 * 250, 2)
    wattage = round(math.sqrt(3) * 210 * ampere * 0.95 / 1000, 2)
    device = int(data[6], 16)

    return (date_time.strftime("%Y-%m-%d %H:%M:%S"),
            sequence_number,
            sigfox_device_id,
            site_id,
            format_version,
            voltage,
            ampere,
            wattage,
            device)


if __name__ == '__main__':
    doctest.testmod()
