from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import rep_keb_n
from dotenv import load_dotenv
import os
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
user_router = Router()





@user_router.message(Command("start"))
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, f"""Начало работы бота помошника. 
Этот бот будет напоминать тебе о твоих тренировках каждый день. 
Так же можно отключить оповещение отдыха. 
Но для начало надо заполнить твой план тренировок для коректной работы.""", reply_markup=rep_keb_n())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')
    



@user_router.message(Command("help"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'помощь')









