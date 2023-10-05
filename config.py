from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.getenv("TOKEN_KEY")

keys = {
    '$': 'USD',
    '€': 'EUR',
    '￡': 'GBP',
    '¥': 'JPY',
    '₽': 'RUB'
}

load_dotenv()

