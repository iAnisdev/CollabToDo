import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASH_KEY = os.getenv('FLASH_KEY')
