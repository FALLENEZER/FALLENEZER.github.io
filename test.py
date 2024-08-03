import telebot

bot = telebot.TeleBot('7278409546:AAEzPe-WB5ePH9luglw_IhLHADZBlWpKgds')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в наш магазин!')

bot.polling(non_stop=True)