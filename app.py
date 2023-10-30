from flask import Flask, json, request, jsonify


app = Flask(__name__)


@app.route('/shortener', methods=['POST'])
def get_url():

    return jsonify({"success": "true"})


if __name__ == '__main__':
    app.run()
