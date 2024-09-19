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
Но для начало надо заполнить твой план тренировок для коректной работы. Нажми /help чтобы у знать о командах бота""", reply_markup=rep_keb_n())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')
    



@user_router.message(Command("help"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Главные команды бота:
1)/addschedule вы можете добавить план тренировок
2)/allschedule бот присылает полный тренировочный план
3)/delschedule вы можете удалить расписание и заполнить занаво
4)/schedule перед вами появится клавиатура с днями неделями и вы модете узнать что вы делаете в конкретный день""")









