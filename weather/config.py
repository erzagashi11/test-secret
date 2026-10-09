import os

# The key is read from the environment; never commit it.
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY", "")
WEATHER_API_URL = "https://api.example-weather.test/v1/forecast"
