import os
from flask import Flask, request, jsonify
import stripe
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route('/create-payment-link', methods=['POST'])
def create_payment_link():
    data = request.get_json()
    try:
        # Example: dynamic price ID and quantity
        price_id = data.get('price_id')
        quantity = data.get('quantity', 1)

        payment_link = stripe.PaymentLink.create(
            line_items=[{"price": price_id, "quantity": quantity}]
        )
        return jsonify({'url': payment_link.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return 'Stripe Payment Link API is live!'

if __name__ == '__main__':
    app.run(debug=True)

