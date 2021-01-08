import telebot
TOKEN = '1070685674:AAFSr950QKddJ97GJNf2qAjICFWQSwjo9U8'
bot= telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welkome(mess):
    bot.send_message(mess.chat.id, 'Я работаю')

bot.polling(none_stop=True)
