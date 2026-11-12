from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/payments', methods=['POST'])
def create_payment():

    data = request.get_json(silent=True) or {}

    user_id = data.get('user_id')
    amount = data.get('amount')

    if user_id is None or amount is None:
        return jsonify({
            "error": "user_id and amount are required"
        }), 400

    if not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({
            "error": "amount must be a positive number"
        }), 400

    return jsonify({
        "transaction_id": "TXN1001",
        "user_id": user_id,
        "amount": amount,
        "status": "SUCCESS"
    }), 201


@app.route('/health')
def health():
    return jsonify({"status": "UP"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
