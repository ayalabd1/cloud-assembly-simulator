import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import certifi

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection string from environment variables
MONGO_URL = os.getenv("MONGO_URL")

# Fallback error check
if not MONGO_URL:
    raise ValueError("MONGO_URL is missing from environment variables!")

# Initialize Async MongoDB Client with certifi SSL certificate fix
client = AsyncIOMotorClient(MONGO_URL, tlsCAFile=certifi.where())

# Select Database and Collection
db = client["assembly_simulator_db"]
history_collection = db["simulation_history"]