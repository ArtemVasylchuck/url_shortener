from flask import Flask, json, request, jsonify
import keygen
from db_config import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///urls.db"

db.init_app(app)

@app.route('/shortener', methods=['POST'])
def get_url():
    data = request.json
    url = data.get("url")
    url_hash = keygen.create_random_key()
    return jsonify({"success": "true",
                    "initial_url": url,
                    "new_url": url_hash})


if __name__ == '__main__':
    app.run(debug=True)
