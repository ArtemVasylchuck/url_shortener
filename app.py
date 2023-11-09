from flask import Flask, json, request, jsonify, redirect

import keygen

import redis

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/shortener', methods=['POST'])
def get_url():
    data = request.json
    url = data.get("url")
    url_hash = keygen.create_random_key()
    r.set(url_hash, url)
    return jsonify({"success": "true",
                    "initial_url": url,
                    "new_url": url_hash})


@app.route('/s/<uri>/', methods=['GET'])
def redirect_url(uri):
    url = r.get(uri)
    print(url)
    return redirect(url)


if __name__ == '__main__':
    app.run(debug=True)