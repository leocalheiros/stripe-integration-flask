import os
from flask import Flask
from src.config.stripe_config import stripe_config
from src.main.routes.stripe_routes import stripe_routes_bp
from src.main.routes.user_routes import user_routes_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config.update(stripe_config)

app.register_blueprint(stripe_routes_bp)
app.register_blueprint(user_routes_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
