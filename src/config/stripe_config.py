import os
from dotenv import load_dotenv
load_dotenv()

stripe_config = {
    "STRIPE_PUBLIC_KEY": os.getenv("STRIPE_PUBLIC_KEY"),
    "STRIPE_SECRET_KEY": os.getenv("STRIPE_SECRET_KEY")
}
