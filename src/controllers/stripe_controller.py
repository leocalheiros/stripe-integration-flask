from flask import url_for
import stripe
from src.config.stripe_config import stripe_config

stripe.api_key = stripe_config['STRIPE_SECRET_KEY']


def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            #List all products
            line_items=[
                {
                    'price': 'price_1OG2XALzFZv0LfHqlMh6JdD1',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=url_for('stripe_routes.thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('stripe_routes.failure', _external=True),
        )
        return checkout_session
    except Exception as e:
        return None


def create_checkout_session_for_product(product_price_id):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product_price_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('stripe_routes.thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('stripe_routes.failure', _external=True),
        )
        return checkout_session
    except Exception as e:
        return None
