from aiogram import Bot, Dispatcher, executor, md, types
from config import TOKEN
from markovLogic import getRandText , saveText

api = Bot(token = TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(api)



# @dp.message_handler(commands=["asd"]) 
# async def echo_all(message):
#     await api.send_message(chat_id=message.chat.id, text=f"{message.from_user.username} said: {message.text}")

@dp.message_handler(commands=["test"])
async def get_random_phrase(message):
    await message.reply(getRandText())

# @dp.message_handler(regexp="(Да)")
# async def get_random_phrase(message):
#     await message.reply("Пизда")

@dp.message_handler(regexp=".*") 
async def echo_all(message):
    print(message.text)
    saveText(message.text)
    








executor.start_polling(dp, skip_updates=True)