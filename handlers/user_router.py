from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv, key_day
from dotenv import load_dotenv
from fun_bd import obnul
import os
from aiogram.types import FSInputFile
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
user_router = Router()


@user_router.message(Command("start"))
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, f"""Начало работы бота помошника. 
Этот бот будет напоминать тебе о твоих тренировках каждый день. 
Но для начала надо заполнить твой план тренировок для коректной работы. Нажми /help чтобы у знать о командах бота""", reply_markup=kebn())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')






@user_router.message(Command("ooobnul"))
async def command_start(message:types.Message):
    obnul()


@user_router.message(Command("help"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Главные команды бота:
1. /work_schedule вызывает клавиатуру с функциями добавления и изменения расписания, она имеет в себе такие функции:
1) /add_schedule вы можете добавить план тренировок
2) /add_schedule_time вы можете добавить тренировки и время сразу
3) /time_change вы можете или добавить или изменить время
4) /change_train вы можете ищменить тренировку в конкретный день
                           
2. /watch_schedule вызывает клавиатуру для просмотра всего расписания а так же его удаления, она имеет в себе такие функции:
1) /all_schedule бот присылает полный тренировочный план
2) /del_schedule вы можете удалить расписание и заполнить занаво
3) /schedule перед вами появится клавиатура с днями неделями и вы модете узнать что вы делаете в конкретный день
скоро будет добавленна функция автоматического отправления рассписания

3. /Template присылает вам файл-шаблон в который вы можете написать свои тренировки и отравить боту. Он вставит их в бд без использования других функций.
Вставляйте ваши тренировки строго в скобочки, иначе будет ошибка.""", reply_markup=kebn())


@user_router.message(Command("work_schedule"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды добавления и изменения расписания""", reply_markup=kebad())

@user_router.message(Command("watch_schedule"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды просмотра расписания""", reply_markup=kebv())


@user_router.message(Command("back"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Назад""", reply_markup=kebn())


@user_router.message(Command("Template"))
async def template(message: types.Message):
    # Указываем путь к файлу
    file_path = 'template.txt'
    
    # Создаем объект FSInputFile
    document = FSInputFile(file_path)
    
    # Отправляем документ пользователю
    await bot.send_document(message.from_user.id, document)




@user_router.message(Command("salaaaaaaaam"))
async def help(message: types.Message):
    sall = FSInputFile('salamchik.jpg')
    await bot.send_photo(message.from_user.id, sall)



