import requests

API_KEY = "*****************" # Your own API_KEY, we added only for test purposes. Please use .env files.
url_weather = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"

city_name = "Istanbul"
country_code = "TR"
url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={API_KEY}"

response = requests.get(url_geo)

response.status_code

data = response.json()
lat = data[0]["lat"]
lon = data[0]["lon"]

url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
response = requests.get(url_weather)
response.status_code

data = response.json()
data
