
from flask import Flask, jsonify, request, render_template
import urllib.request
import json

app = Flask(__name__)

# Frontend dashboard
@app.route('/')
def home():
    return render_template('index.html')


# Gateway -> User Service
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    try:
        url = f"http://user-service:8082/users/{user_id}"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        return jsonify(data)

    except Exception as error:
        return jsonify({"error": str(error)}), 502


# Gateway -> Payment Service
@app.route('/api/payments', methods=['POST'])
def make_payment():
    try:
        data = request.get_json(silent=True) or {}

        payment_url = "http://payment-service:8081/payments"

        payment_data = json.dumps(data).encode()

        payment_request = urllib.request.Request(
            payment_url,
            data=payment_data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(payment_request) as response:
            result = json.loads(response.read().decode())

        return jsonify(result), 201

    except Exception as error:
        return jsonify({"error": str(error)}), 502


@app.route('/health')
def health():
    return jsonify({"status": "UP"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
