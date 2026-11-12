from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users/<int:user_id>')
def get_user(user_id):

    user = {
        "user_id": user_id,
        "name": "Vamshi",
        "account_status": "ACTIVE"
    }

    return jsonify(user)

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
