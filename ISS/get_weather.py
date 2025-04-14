import urllib.request
import json

def get_weather(lat, lon):
    """
    Get the weather at a given location
    """
    key = 'b5c4f65608ce882fd5cf839e8878a0ad'
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result
