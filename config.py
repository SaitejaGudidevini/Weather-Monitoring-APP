import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and Services
WEATHER_API_KEY = "5e867aa58a84a3adf87d4522483be843"
EMAIL_SERVER = os.getenv("EMAIL_SERVER")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "/Users/saitejagudidevini/Documents/Dev/WeatherAPI/weather_monitor/weather_monitor.db")

# Weather Monitoring Settings
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "10"))  # 10 seconds default
FREEZE_THRESHOLD = float(os.getenv("FREEZE_THRESHOLD", "32.0"))  # Fahrenheit
import os

# Email Configuration
EMAIL_SENDER = "saiusual8@gmail.com"  # Replace with your Gmail address
EMAIL_PASSWORD = "hstq zrao odxg hivb"  # Replace with your Gmail App Password

# Load environment variables if they exist
EMAIL_SENDER = os.environ.get('EMAIL_SENDER', EMAIL_SENDER)
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', EMAIL_PASSWORD)
