import os
import telebot

from dotenv import load_dotenv
from get_apis import get_weather, get_exchange

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, "Hello, type /options")

@bot.message_handler(commands = ['options'])
def show_options(message):
	markup = telebot.types.InlineKeyboardMarkup()
	markup.add(telebot.types.InlineKeyboardButton(text='Weather', callback_data='weather'))
	markup.add(telebot.types.InlineKeyboardButton(text='Vaults', callback_data ='exchanger'))
	bot.send_message(message.chat.id, text = 'Choose any option', reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def options(call):
	bot.answer_callback_query(callback_query_id=call.id, text=call.data)
	if call.data == 'weather':
		sent_msg = bot.send_message(call.message.chat.id, 'Enter city name')
		bot.register_next_step_handler(sent_msg, weather)
	elif call.data == 'exchanger':
		sent_msg = bot.send_message(call.message.chat.id, "Enter  vault - to vault - amount")
		bot.register_next_step_handler(sent_msg, exchange)

@bot.message_handler(content_types = ['text'])
def weather(message):
	try:
		weather, degrees = get_weather(message.text)
		bot.send_message(message.chat.id, f"Weather: {weather}, temperature: {degrees}")
	except TypeError:
		bot.send_message(message.chat.id, 'Please, enter correct city name')

@bot.message_handler(content_types = ['text'])
def exchange(message):
	try:
		from_vault, to_vault, amount = message.text.split()
		result = get_exchange(from_vault, to_vault, amount)
		bot.send_message(message.chat.id, f"{amount} {from_vault.upper()} converted to {result} {to_vault.upper()}")
	except TypeError as error:
		bot.send_message(message.chat.id, f'Please, enter correct currency.{error}')
		

bot.polling()