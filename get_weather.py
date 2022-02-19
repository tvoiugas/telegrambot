import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API = os.environ.get('OPENWEATHER_API_KEY')

def get_weather(city):
	url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'

	response = requests.get(url)
	dict_response = json.loads(response.text)
	weather = dict_response.get('weather')[0].get('description')
	degrees = dict_response.get('main').get('temp')
	return weather, degrees
