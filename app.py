from flask import Flask, render_template, request, jsonify
from weather_service import WeatherService
from email_service import EmailService
from geopy.geocoders import Nominatim
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

weather_service = WeatherService()
email_service = EmailService()

def get_location_coordinates(location_name):
    """Get coordinates for a location name using geocoding"""
    try:
        geolocator = Nominatim(user_agent="weather_monitor")
        location = geolocator.geocode(location_name)
        if location:
            return {
                'name': location_name,
                'latitude': location.latitude,
                'longitude': location.longitude
            }
        return None
    except Exception as e:
        logging.error(f"Error geocoding location: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location_name = request.form.get('location')
    email = request.form.get('email')
    
    location_info = get_location_coordinates(location_name)
    if not location_info:
        return jsonify({'error': 'Location not found'})
    
    try:
        weather = weather_service.get_weather(
            location_info['latitude'],
            location_info['longitude']
        )
        
        # Send email if email address is provided
        if email:
            try:
                email_service.send_weather_update(
                    email,
                    location_info['name'],
                    weather['temperature'],
                    weather['description']
                )
            except Exception as e:
                logging.error(f"Error sending email: {e}")
                return jsonify({'error': f'Weather retrieved but email failed: {str(e)}'})
        
        return jsonify({
            'location': location_info['name'],
            'temperature': weather['temperature'],
            'description': weather['description'],
            'email_sent': bool(email)
        })
    except Exception as e:
        logging.error(f"Error getting weather: {e}")
        return jsonify({'error': str(e)})

def cli_interface():
    """Command line interface to get weather updates"""
    print("Welcome to Weather Update Service!")
    
    # Get email
    email = input("Please enter your email address: ").strip()
    
    # Get location
    location_name = input("Enter your preferred location (e.g., 'London, UK'): ").strip()
    
    # Get coordinates
    location_info = get_location_coordinates(location_name)
    if not location_info:
        print("Error: Location not found")
        return
    
    try:
        # Get weather
        weather = weather_service.get_weather(
            location_info['latitude'],
            location_info['longitude']
        )
        
        # Send email
        email_service.send_weather_update(
            email,
            location_info['name'],
            weather['temperature'],
            weather['description']
        )
        
        print(f"\nWeather update for {location_info['name']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"\nWeather update has been sent to {email}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        cli_interface()
    else:
        app.run(debug=True)
