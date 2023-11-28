import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "DATABASE_URL": os.getenv("DATABASE_URL"),
}
