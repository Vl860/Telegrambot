import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import currencies

# token from BotFather
bot = Bot(token="Your token")

# initialize dispatcher
dp = Dispatcher(bot)

# configure logging
logging.basicConfig(level=logging.INFO)


# start command
@dp.message_handler(commands="start")
async def welcome(message: types.Message):
    # getting username (if user does not have a username, his full name will be returned
    username = message.from_user.mention

    await message.answer(f"Hello there {username} 👋\n\n"
                         f"My name is Testbot\n\n"
                         f"If you want to start, type in /get\n\n"
                         f"If you need more info, type in /help")


# help command
@dp.message_handler(commands="help")
async def helping(message: types.Message):
    await message.answer("All currencies are considered in\nSwiss francs(CHF) 🇨🇭")


# get command(shows buttons)
@dp.message_handler(commands="get")
async def helping(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["💰 Get the whole list",
               "🇺🇸 U.S. dollar",
               "🇪🇺 Euro",
               "🇯🇵 Japanese yen",
               "🇬🇧 Pound sterling",
               "🇦🇺 Australian dollar",
               "🇨🇦 Canadian dollar",
               "🇭🇰 Hong Kong dollar",
               "🇳🇿 New Zealand dollar"]
    keyboard.add(*buttons)
    await message.answer("Please select an option:", reply_markup=keyboard)


# the whole list command (sends prices of all 8 currencies)
@dp.message_handler(Text(equals="💰 Get the whole list"))
async def get_all(message: types.Message):
    await message.answer(f"🇺🇸 1 US-Dollar = {currencies.USD.value} CHF 🇨🇭\n\n"
                         f"🇪🇺 1 EUR = {currencies.EUR.value} CHF 🇨🇭\n\n"
                         f"🇯🇵 1 Japanese yen = {currencies.JPY.value} CHF 🇨🇭\n\n"
                         f"🇬🇧 1 Pound sterling = {currencies.GBP.value} CHF 🇨🇭\n\n"
                         f"🇦🇺 1 Australian dollar = {currencies.AUD.value} CHF 🇨🇭\n\n"
                         f"🇨🇦 1 Canadian dollar = {currencies.CAD.value} CHF 🇨🇭\n\n"
                         f"🇭🇰 1 Hong Kong dollar = {currencies.HKD.value} CHF 🇨🇭\n\n"
                         f"🇳🇿 1 New Zealand dollar = {currencies.NZD.value} CHF 🇨🇭")


# US dollar price command
@dp.message_handler(Text(equals="🇺🇸 U.S. dollar"))
async def USDprice(message: types.Message):
    await message.answer(f"🇺🇸 1 US-Dollar = {currencies.USD.value} CHF 🇨🇭")


# Euro price command
@dp.message_handler(Text(equals="🇪🇺 Euro"))
async def EURprice(message: types.Message):
    await message.answer(f"🇪🇺 1 EUR = {currencies.EUR.value} CHF 🇨🇭")


# Japanese yen price command
@dp.message_handler(Text(equals="🇯🇵 Japanese yen"))
async def JPYprice(message: types.Message):
    await message.answer(f"🇯🇵 1 Japanese yen = {currencies.JPY.value} CHF 🇨🇭")


# Pound sterling price command
@dp.message_handler(Text(equals="🇬🇧 Pound sterling"))
async def GBPprice(message: types.Message):
    await message.answer(f"🇬🇧 1 Pound sterling = {currencies.GBP.value} CHF 🇨🇭")


# Australian dollar price command
@dp.message_handler(Text(equals="🇦🇺 Australian dollar"))
async def AUDprice(message: types.Message):
    await message.answer(f"🇦🇺 1 Australian dollar = {currencies.AUD.value} CHF 🇨🇭")


# Canadian dollar price command
@dp.message_handler(Text(equals="🇨🇦 Canadian dollar"))
async def CADprice(message: types.Message):
    await message.answer(f"🇨🇦 1 Canadian dollar = {currencies.CAD.value} CHF 🇨🇭")


# Hong Kong dollar price command
@dp.message_handler(Text(equals="🇭🇰 Hong Kong dollar"))
async def HKDprice(message: types.Message):
    await message.answer(f"🇭🇰 1 Hong Kong dollar = {currencies.HKD.value} CHF 🇨🇭")


# New Zealand dollar price command
@dp.message_handler(Text(equals="🇳🇿 New Zealand dollar"))
async def NZDprice(message: types.Message):
    await message.answer(f"🇳🇿 1 New Zealand dollar = {currencies.NZD.value} CHF 🇨🇭")



# unknown command (If user uses an unknown command, the function is triggered)
@dp.message_handler()
async def unknown_command(message: types.Message):
    await message.answer("I don't know what to do with that command 😕")




# bot launch 
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
