from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv, key_day
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
Но для начало надо заполнить твой план тренировок для коректной работы. Нажми /help чтобы у знать о командах бота""", reply_markup=kebn())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')


@user_router.message(Command("help"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Главные команды бота:
1. /add вызывает клавиатуру с функциями добавления и изменения расписания, она имеет в себе такие функции:
1) /addschedule вы можете добавить план тренировок
2) /addscheduletime вы можете добавить тренировки и время сразу
3) /time_change вы можете или добавить или изменить время
4) /change_train_day вы можете ищменить тренировку в конкретный день
                           
2. /schedule_w вызывает клавиатуру для просмотра всего расписания а так же его удаления, она имеет в себе такие функции:
1) /allschedule бот присылает полный тренировочный план
2) /delschedule вы можете удалить расписание и заполнить занаво
3) /schedule перед вами появится клавиатура с днями неделями и вы модете узнать что вы делаете в конкретный день
скоро будет добавленна функция автоматического отправления рассписания""", reply_markup=kebn())


@user_router.message(Command("add"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды добавления и изменения расписания""", reply_markup=kebad())

@user_router.message(Command("schedule_w"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды просмотра расписания""", reply_markup=kebv())









