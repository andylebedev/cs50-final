import sys
import requests

def main():
  city = get_city()
  latitude, longitude = get_coordinates(city)
  get_weather(latitude, longitude, city)

def get_city():
  if len(sys.argv) != 2:
    try:
        city = str(input("What is your city: ")).lower()
    except ValueError:
        print("City name is expected")
  else:
     city = sys.argv[1].lower()
  return city

def get_coordinates(city):
  try:
    r = requests.get(f'https://geocode.maps.co/search?q={city}' )
    data = r.json()
  except requests.RequestException: sys.exit("Your city not found")
  latitude = data[1]['lat']
  longitude = data[1]['lon']
  return latitude[:7], longitude[:7]


def get_weather(latitude, longitude, city):
  try:
    w = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
    weather_data = w.json()
  except requests.RequestException: sys.exit("Your city not found")
  temperature = weather_data['current_weather']['temperature']
  temperature_unit = weather_data['current_weather_units']['temperature']
  print(f"Current temperature in {city.lower().capitalize()} is {temperature} {temperature_unit}")


if __name__ == "__main__":
  main()
