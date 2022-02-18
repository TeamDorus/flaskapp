import os
import dotenv

dotenv.load_dotenv('.env')


class Config:
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  SECRET_KEY = os.environ.get('SECRET_KEY')

  TRACCAR_BASE_URL = os.environ.get('TRACCAR_BASE_URL')
  TRACCAR_API_USER = os.environ.get('TRACCAR_API_USER')
  TRACCAR_API_PASS = os.environ.get('TRACCAR_API_PASS')

  TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
  TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

