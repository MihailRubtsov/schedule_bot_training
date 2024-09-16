from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from handlers.keybooards import rep_keb_n
from handlers.keybooards import key_day
import sys
import sqlite3
import os
import sys
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
rasp_router = Router()




@rasp_router.message(Command("schedule"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'расписание', reply_markup= key_day())



@rasp_router.message(Command("Friday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())