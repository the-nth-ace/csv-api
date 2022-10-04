import os
import motor.motor_asyncio
from dotenv import load_dotenv
from app.schemas.config import ConfigSettings

load_dotenv()
MONGO_URL = os.environ.get("MONGO_URL")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.business
series_collection = database.get_collection("series_collection")
