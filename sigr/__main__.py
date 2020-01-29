"""Mainモジュール

* Sigfox cloud コールバックの待ち受け
* データの解析
* データベースへの登録処理

Todo:
    * None
"""
from flask import Flask, request, make_response

import sigr.client
import sigr.parser
import sigr.database

app = Flask(__name__)


@app.route('/api/v1/receive', methods=['POST'])
def receiver():
    """ Sigfoxからのコールバックデータを待ち受ける

    コールバックデータを受信したら、データを解析してデータベースに登録処理を行う。
    """
    json_data = request.get_json()
    parsed_data = sigr.parse_payload_data(json_data)

    print(json_data)
    print(parsed_data)

    # Insert DB
    db = sigr.Database()
    db.insert_parsed_data_in_db(parsed_data)

    response = make_response('Response Object')
    response.headers['X-datatype'] = type(response)
    return response


@app.route('/api/v1/<sigfox_device_id>/messages')
def show_messages(sigfox_device_id):
    """指定されたデバイスのSigfoxメッセージ一覧を表示

    Args:
        sigfox_device_id (str): SigfoxデバイスのID
    """
    client = sigr.Client()
    return client.get_messages(sigfox_device_id)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
