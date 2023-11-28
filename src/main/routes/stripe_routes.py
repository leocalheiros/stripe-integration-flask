from flask import Flask, render_template, redirect, url_for, request
from src.config.stripe_config import stripe_config
from src.controllers.stripe_controller import create_checkout_session, create_checkout_session_for_product
import stripe

app = Flask(__name__)

app.config.update(stripe_config)


def is_checkout_session_successful(session_id):
    try:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        return checkout_session['payment_status'] == 'paid'
    except stripe.error.StripeError as e:
        return False


@app.route('/index')
def index():
    checkout_session = create_checkout_session()
    if not checkout_session:
        return "Failed to create checkout session."

    return render_template('index.html')


@app.route('/stripe_pay')
def stripe_pay():
    # Change this for your product_id logic
    checkout_session = create_checkout_session_for_product('price_1OG2XALzFZv0LfHqlMh6JdD1')
    if not checkout_session:
        return "Failed to create checkout session for product."

    return {
        'checkout_session_id': checkout_session['id'],
        'checkout_public_key': app.config['STRIPE_PUBLIC_KEY']
    }


@app.route('/thanks')
def thanks():
    session_id = request.args.get('session_id')
    if not session_id or not is_checkout_session_successful(session_id):
        return redirect(url_for('failure'))

    return render_template('thanks.html')


@app.route('/failure')
def failure():
    return render_template('failure.html')
