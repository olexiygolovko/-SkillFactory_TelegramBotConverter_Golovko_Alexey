from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.getenv('TOKEN_KEY') #your token should be here

keys = {
    '$': 'USD',
    '€': 'EUR',
    '￡': 'GBP',
    '¥': 'JPY',
    '₽': 'RUB'
}

load_dotenv()


