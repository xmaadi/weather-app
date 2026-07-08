# Weather App 🌤️

A Python CLI project to fetch real-time weather data using OpenWeatherMap API.

## Features

- Fetch live weather by city name
- Shows temperature, feels-like, humidity, condition, wind speed
- Error handling for invalid city names and API key issues
- Clean formatted CLI output

## Built With

- Python (Pydroid 3 on Android)
- Requests library
- OpenWeatherMap API

## Setup

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)
2. Create a file `api_key.py` with:
   ```python
   API_KEY = "your_api_key_here"
