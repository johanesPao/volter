import os
from dotenv import load_dotenv
from dataclasses import dataclass
from urllib.parse import quote

load_dotenv()


@dataclass
class ExchangeAPI:
    KEY: str
    SECRET_KEY: str


@dataclass
class ParameterDB:
    HOST: str
    PORT: str
    USERNAME: str
    PASSWORD: str
    DATABASE: str


TZ = 7  # timezone

API = ExchangeAPI(KEY=os.getenv("API_KEY"), SECRET_KEY=os.getenv("API_SECRET_KEY"))

DB = ParameterDB(
    HOST=os.getenv("DB_HOST"),
    PORT=os.getenv("DB_PORT"),
    USERNAME=os.getenv("DB_USER"),
    PASSWORD=os.getenv("DB_PASS"),
    DATABASE=os.getenv("DB_NAME"),
)

DATABASE_URL = (
    f"postgresql://{DB.USERNAME}:{quote(DB.PASSWORD)}@database:{DB.PORT}/{DB.DATABASE}"
)

ENV_MODE = os.getenv("ENV_MODE")

INTERVAL_CEK = 20  # detik
