1.	🚀 Project: ISS Location, Weather, and Distance Finder
Tech Stack: Python, Flask, Open Notify API, OpenWeatherMap API, Google Maps Distance API
Project Overview:
This Flask web application integrates multiple real-time APIs to provide users with live information about the International Space Station (ISS), including:
•	The ISS's current coordinates
•	The city and weather at the ISS's location
•	The distance from the ISS to a user-defined city (e.g., Halifax)
Key Features & Data Flow:
1.	Open Notify API is used to fetch the ISS's real-time latitude and longitude coordinates.
2.	OpenWeatherMap API retrieves weather data at the ISS's current location (temperature, weather conditions).
3.	Google Maps Distance Matrix API calculates the distance between the ISS’s position and a target city using geographical coordinates.
4.	Flask handles user input via a web form and dynamically updates the results by combining data from all three APIs.
Behind the Scenes:
•	When a user enters a city (like "Halifax") and submits the form, the server performs three back-to-back API calls.
•	Coordinates are extracted from Open Notify's JSON response.
•	These coordinates are passed to OpenWeatherMap to get contextual weather data (e.g., "light clouds, 17°C").
•	Simultaneously, the Google Maps Distance API calculates the distance in kilometers between the ISS and the input location.
•	All results are displayed neatly on a rendered HTML page, which is dynamically generated using Flask.
