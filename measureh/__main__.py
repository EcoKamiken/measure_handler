import measureh.client
import measureh.parser
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "index"


@app.route('/api/v1/receive', methods=['POST'])
def receiver():
    """ Sigfoxからのコールバックデータを待ち受ける

    コールバックデータを受信したら、データを解析してデータベースに登録処理を行う。
    """
    json_data = request.get_json()
    data = measureh.parser.parse_payload_data(json_data)
    print(data)
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
