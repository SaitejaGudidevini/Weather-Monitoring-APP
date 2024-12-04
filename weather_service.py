import requests
from config import WEATHER_API_KEY

class WeatherService:
    def __init__(self):
        self.api_key = WEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, lat, lon):
        """Get current weather for a location"""
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'imperial'  # For Fahrenheit
        }
        
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'conditions': data['weather'][0]['main'],
            'description': data['weather'][0]['description']
        }
