import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
