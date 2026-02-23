import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError("API key and secret must be set in .env file")

        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _sign(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, **kwargs) -> dict:
        endpoint = "/fapi/v1/order"
        url = BASE_URL + endpoint
        params = self._sign(kwargs)

        logger.info(f"Sending order request: {kwargs}")

        try:
            response = self.session.post(url, params=params)
            data = response.json()

            if response.status_code == 200:
                logger.info(f"Order response: {data}")
            else:
                logger.error(f"API error: {data}")

            return data

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise