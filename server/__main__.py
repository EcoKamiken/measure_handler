from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/mfa/api/v0.1/messages', methods=['POST'])
def parser():
    j = request.get_json()
    return jsonify(j)


if __name__ == '__main__':
    app.run(debug=True)
