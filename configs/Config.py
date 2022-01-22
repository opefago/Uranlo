import os
from dotenv import load_dotenv
load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
keys = dict(
    CONSUMER_KEY=os.environ.get("CONSUMER_KEY"),
    CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET"),
    ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN"),
    ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
)

MONGODR_URI = os.environ.get("MONGODB_URI")
