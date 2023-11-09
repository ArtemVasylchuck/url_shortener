from flask import Flask, json, request, jsonify, redirect

import redis

import keygen

from utils import url_beatify, make_absolute_path_from_uri

from pydantic import ValidationError

from response_model import UrlModel

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.route('/shortener', methods=['POST'])
def get_url():
    data = request.json
    url = data.get("url")

    try:
        UrlModel(url=url)
    except ValidationError:
        url = url_beatify(url)

    url_hash = keygen.create_random_key()
    full_url = make_absolute_path_from_uri(url_hash)

    while True:
        if r.get(url_hash):
            url_hash = keygen.create_random_key()
        else:
            break

    r.set(url_hash, url)

    return jsonify({"status": "200",
                    "data": {
                        "initial_url": url,
                         "new_url": full_url
                    }})


@app.route('/s/<uri>/', methods=['GET'])
def redirect_url(uri):
    url = r.get(uri)
    return redirect(url)


if __name__ == '__main__':
    app.run(debug=True)