"""Mainモジュール

* Sigfox cloud コールバックの待ち受け
* データの解析
* データベースへの登録処理

Todo:
    * None
"""
import doctest

from flask import Flask, request

import measureh.client
import measureh.parser
import measureh.database

app = Flask(__name__)


@app.route('/')
def index():
    return "index"


@app.route('/api/v1/receive', methods=['POST'])
def receiver():
    """ Sigfoxからのコールバックデータを待ち受ける

    コールバックデータを受信したら、データを解析してデータベースに登録処理を行う。
    """
    db = measureh.database.Database()
    json_data = request.get_json()
    data = measureh.parser.parse_payload_data(json_data)
    db.sigfox_tuple_insert_to_db(data)
    return json_data


@app.route('/api/v1/<sigfox_device_id>/messages')
def show_messages(sigfox_device_id):
    """ 引数で指定したデバイスのsigfoxメッセージ一覧を表示

    Args:
        sigfox_device_id (str): SigfoxデバイスのID
    """
    client = measureh.client.Client()
    return client.get_messages(sigfox_device_id)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
    doctest.testmod()
