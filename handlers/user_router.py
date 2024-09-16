from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.keybooards import rep_keb_n
from handlers.keybooards import key_day
from dotenv import load_dotenv
import sys
import sqlite3
import os
import sys
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



@user_router.message(Command("help"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'помощь')





