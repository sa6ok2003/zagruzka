from aiogram import Bot, Dispatcher,executor,types
TOKEN = '1070685674:AAFSr950QKddJ97GJNf2qAjICFWQSwjo9U8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,'Hello')

if __name__ == "__main__":
    executor.start_polling(dp)