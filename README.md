# Weather Monitor Application

A Flask-based web application that provides real-time weather information for any location using geocoding and weather services.

## Features

- Location-based weather information
- Real-time temperature and weather description
- Geocoding support for location search
- Simple and intuitive web interface

## Prerequisites

Before running this application, make sure you have Python 3.x installed and the following packages:

```bash
pip install flask
pip install geopy
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/SaitejaGudidevini/Weather-Monitoring-APP.git
cd weather_monitor
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The application uses the following services:
- Nominatim for geocoding (no API key required)
- Weather service (configure in weather_service.py)

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

### GET /
- Renders the main page with the weather search interface

### POST /get_weather
- Accepts form data with a 'location' parameter
- Returns weather information in JSON format
- Example response:
```json
{
    "location": "New York",
    "temperature": 20.5,
    "description": "Partly cloudy"
}
```

## Error Handling

The application includes error handling for:
- Invalid locations
- Geocoding failures
- Weather service errors

All errors are logged using Python's logging module.

## Project Structure

```
weather_monitor/
├── app.py              # Main Flask application
├── weather_service.py  # Weather service integration
└── templates/         
    └── index.html      # Main page template
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
