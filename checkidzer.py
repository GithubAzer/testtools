import requests
import telebot
import random
from telebot import types
bot = telebot.TeleBot("5294987313:AAHbRwkvbrVOl_CiGWbNIYqzDxeBEvxTsyA")

p = types.InlineKeyboardButton(text = "Telegram", url = 't.me/ZERTOOLS')

@bot.message_handler(commands=['start'])
def start(message):
	SD = types.InlineKeyboardMarkup()
	SD.row_width = 1
	SD.add(p)
	frt = message.chat.first_name
	bot.send_message(message.chat.id, text=f"""- اهلاً بك ( {frt} )
- في بوت فحص ايديات انستا اب .
- رجاءً قم ب ارسال instaupid .
- Bot by : @ZERTOOLS""",reply_markup=SD)
@bot.message_handler(func=lambda m:True)

def start(message):
	try:
		msg = message.text
		bot.send_message(message.chat.id,'''WAIT PLEASE . . .''')
		api = f'https://chheck.thth9.repl.co/?oid={msg}&submit=submit'
		req = requests.get(api).text
		if 'coins":"' in req:
			Check = req.split('coins":"')[1]
			coin = Check.split('"')[0]
			bot.send_message(message.chat.id,f'''{msg}-{coin}''')
		else:
			bot.send_message(message.chat.id,f'''{msg}-block''')
	except:
		pass

bot.polling()