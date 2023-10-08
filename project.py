import sys
import requests

def main():
  print("Hello %username%")
  latitude, longitude = get_user_city()
  weather_alert(latitude, longitude)
  what_is_weather(latitude, longitude)
  forecast(latitude, longitude)

def get_user_city():
  if len(sys.argv) != 2:
    try:
        city = str(input("What is your city: "))
    except ValueError:
        print("City name is expected")
  else:
     city = sys.argv[1]
  try:
    r = requests.get(f'https://geocode.maps.co/search?q={city}' )
    data = r.json()
  except requests.RequestException: sys.exit("Your city not found")
  latitude = data[1]['lat']
  longitude = data[1]['lon']
  return latitude[:7], longitude[:7]
  

def what_is_weather(latitude, longitude):
  try:
    w = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={latitude}&current_weather=true')
    weather_data = w.json()
  except requests.RequestException: sys.exit("Your city not found")
  print(weather_data)
  temperature = weather_data['current_weather']
  print(temperature)

def forecast(latitude, longitude):
  ...

def weather_alert(latitude, longitude):
   ...

if __name__ == "__main__":
  main()
