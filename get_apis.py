import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.environ.get('OPENWEATHER_API_KEY')
EXCHANGE_API = os.environ.get('EXCHANGE_RATE')

def get_weather(city):
	url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}'

	response = requests.get(url)
	dict_response = json.loads(response.text)
	weather = dict_response.get('weather')[0].get('description')
	degrees = dict_response.get('main').get('temp')
	return weather, degrees


def get_exchange(from_vault, to_vault, amount):
	from_vault = from_vault.upper()
	to_vault = to_vault.upper()
	url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API}/latest/{from_vault}"

	response = requests.get(url)
	dict_response = json.loads(response.text)
	rates = dict_response.get('conversion_rates')
	result = rates.get(to_vault)
	return result * int(amount)