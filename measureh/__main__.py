import measureh.client
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "index"


@app.route('/api/v1/receive', methods=['POST'])
def receiver():
    j = request.get_json()
    print(j)
    return jsonify(j)


@app.route('/api/v1/<sigfox_device_id>/messages')
def show_messages(sigfox_device_id):
    client = measureh.client.Client()
    return client.get_messages(sigfox_device_id)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
