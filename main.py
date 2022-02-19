from dotenv import load_dotenv
import os
import telebot
from get_weather import get_weather

load_dotenv()
token = os.environ.get('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
	markup = telebot.types.InlineKeyboardMarkup()
	bot.send_message(message.chat.id, "Yo, what's up?")
	markup.add(telebot.types.InlineKeyboardButton(text='Погода', callback_data='weather'))
	markup.add(telebot.types.InlineKeyboardButton(text='Валюты', callback_data ='exchanger'))
	bot.send_message(message.chat.id, text = 'Choose any option', reply_markup = markup)

# @bot.message_handler(content_types = ['text'])
# def echo(message):
# 	bot.send_message(message.chat.id, message.text)

@bot.callback_query_handler(func=lambda call: True)
def options(call):
	bot.answer_callback_query(callback_query_id=call.id, text='weather')

bot.polling()