from flask import Blueprint, render_template, redirect, url_for, request, session
from src.controllers.stripe_controller import create_checkout_session, create_checkout_session_for_product
from src.config.stripe_config import stripe_config
import stripe

stripe_routes_bp = Blueprint("stripe_routes", __name__)


def is_checkout_session_successful(session_id):
    try:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        return checkout_session['payment_status'] == 'paid'
    except stripe.error.StripeError as e:
        return False


@stripe_routes_bp.route('/index')
def index():
    if not 'user_id' in session:
        return redirect(url_for('user_routes.login_page'))
    checkout_session = create_checkout_session()
    if not checkout_session:
        return "Failed to create checkout session."

    return render_template('index.html')


@stripe_routes_bp.route('/stripe_pay')
def stripe_pay():
    checkout_session = create_checkout_session_for_product('price_1OG2XALzFZv0LfHqlMh6JdD1')
    if not checkout_session:
        return "Failed to create checkout session for product."

    return {
        'checkout_session_id': checkout_session['id'],
        'checkout_public_key': stripe_config['STRIPE_PUBLIC_KEY']
    }


@stripe_routes_bp.route('/thanks')
def thanks():
    session_id = request.args.get('session_id')
    if not session_id or not is_checkout_session_successful(session_id):
        return redirect(url_for('stripe_routes.failure'))

    return render_template('thanks.html')


@stripe_routes_bp.route('/failure')
def failure():
    return render_template('failure.html')
