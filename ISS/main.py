from flask import Flask,render_template
from get_iss import iss_loc
from get_weather import get_weather
from get_address import address
from get_distance import dist
from get_country import country

app = Flask('app')
#adding endpoints to connect to the html files
@app.route('/')
def hello_world():
  #getting longitudes and lattitudes for the space station
  data = iss_loc()
  lat, lon = data[0], data[1]
  position = [f"Latitude: {lat}, Longitude: {lon}"]

  #getting weather below the space station
  weather = get_weather(lat, lon)
  temp_c = round(weather["main"]["temp"] - 273.15,2)
  desc = weather["weather"][0]['description']
  weather_final = (str(temp_c)+"C", desc)

  #distance from the iss
  distance = dist(lat,lon,46.4915458,-80.9947947)
  distance_final = f"You are {distance}km from the ISS"

  #address reverse geolocation
  addr = address(lat,lon)
  print("Country code",addr["countryCode"])

  #creating a function to display if the iss is over water or above land
  def iss_fn():
    if addr["countryCode"]== "":
        return 'The ISS is currently over water'
    else:
      # print(addr)
      location = addr['countryCode']
      city = f"City- {addr['city']}, Country - {addr['countryName']}"
      flag = country(location)[0]["flags"]["png"]
      return city, flag

  data = iss_fn()

  return render_template('index.html', position=position, weather_final=weather_final, distance_final=distance_final,data=data)

app.run(host='0.0.0.0', port=8080)
