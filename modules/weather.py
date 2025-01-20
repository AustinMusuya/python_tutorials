"""
Exercise 2: Exploring Python Libraries

Instruction:

Use the requests library to fetch weather information from an online weather API (e.g., weatherapi.

Install the requests library using pip if it’s not already installed pip install requests.

Write a Python script weather.py to use the requests.get method to fetch weather data from the API.

Print out relevant weather information (e.g., temperature, weather description) from the API response.

"""

import requests

api_key = "c153bb55dc22497a9df104027242509"


def fetch_weather(api_key, location):
    # API endpoint for current weather data
    url = "http://api.weatherapi.com/v1/current.json"

    # Parameters for the API request
    payload = {'key': api_key, 'q': location}

    try:
        # Making the request to the API
        response = requests.get(url, params=payload)

        # Print the status code
        print("Status Code:", response.status_code)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract relevant weather information
            location_name = data['location']['name']

            temperature = data['current']['temp_c']  # Temperature in Celsius

            # Weather description
            weather_desc = data['current']['condition']['text']

            # Print the weather information
            print(f"Weather in {location_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {weather_desc}")
        else:
            # Print the error message if the request was not successful
            print("Error:", response.text)

    except Exception as e:
        print("An error occurred:", e)
