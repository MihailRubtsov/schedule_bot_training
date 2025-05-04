from aiogram import Bot, types, Dispatcher, Router , F
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv
from dotenv import load_dotenv
import os
from fun_db import *
from aiogram.types import FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from .nazv_kom import *
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
user_router = Router()


class CBGU(StatesGroup):
    sex = State()
    age = State()
    hight = State()
    weight = State()
    act = State()


class pokup(StatesGroup):
    code = State()


# @user_router.message(Command("start") or F.text.lower() == b_start)
@user_router.message(Command("start"))
async def command_start(message:types.Message):
    if prov_in(message.from_user.id) == False:
        sozd_prof(message.from_user.id)
    await bot.send_message(message.from_user.id, f"""Начало работы бота помощника. 
Этот бот будет напоминать тебе о твоих тренировках каждый день. 
Но для начала надо заполнить твой план тренировок для коректной работы. Нажми /help чтобы у знать о командах бота""", reply_markup=kebn())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')






@user_router.message(Command("ooobnul"))
async def command_start(message:types.Message):
    obnul()

@user_router.message(Command("help"))
# @user_router.message(F.text.lower() == b_help)
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Главные команды бота:
1. /work_schedule вызывает клавиатуру с функциями добавления и изменения расписания, она имеет в себе такие функции:
1) /add_schedule добавление тренировочной недели
2) /add_time добавление времени отправки напоминаний
3) /time_change смена времени отправки напоминаний
4) /change_train изменение тренировочной недели
5) /del_schedule удаление последней тренировочной недели
6) /add_schedule_file добавление недели с помощью файла
                           
2. /watch_schedule вызывает клавиатуру для просмотра всего расписания, она имеет в себе такие функции:
1) /all_schedule бот присылает полный тренировочный план
2) /schedule_ned просмотр конкретной тренировочной недели

3. /Template присылает вам файл-шаблон в который вы можете написать свои тренировки и отравить боту. Он вставит их в бд без использования других функций.
Вставляйте ваши тренировки строго в скобочки, иначе будет ошибка.""", reply_markup=kebn())


@user_router.message(Command("work_schedule"))
# @user_router.message(F.text.lower() == b_change)
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды добавления и изменения расписания""", reply_markup=kebad())

@user_router.message(Command("watch_schedule"))
# @user_router.message(F.text.lower() == b_watch)
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Команды просмотра расписания""", reply_markup=kebv())

@user_router.message(Command("back"))
# @user_router.message(F.text.lower() == b_back)
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, """Назад""", reply_markup=kebn())

@user_router.message(Command("Template"))
# @user_router.message(F.text.lower() == b_template)
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


@user_router.message(Command('raschot'))
# @user_router.message(F.text.lower() == b_kallor)
async def change_day1(message: types.Message, state:FSMContext):
    await bot.send_message(message.from_user.id, 'Какой у вас пол 1 = м, 2 = ж', reply_markup=kebn())
    await state.set_state(CBGU.sex)

@user_router.message(CBGU.sex)
async def change_day2(message: types.Message, state:FSMContext):

    await state.update_data(sex = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш возраст', reply_markup=kebn())
    await state.set_state(CBGU.age)

@user_router.message(CBGU.age)
async def change_day3(message: types.Message, state:FSMContext):

    await state.update_data(age = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш рост', reply_markup=kebn())
    await state.set_state(CBGU.hight)


@user_router.message(CBGU.hight)
async def change_day4(message: types.Message, state:FSMContext):

    await state.update_data(hight = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш вес', reply_markup=kebn())
    await state.set_state(CBGU.weight)


@user_router.message(CBGU.weight)
async def change_day5(message: types.Message, state:FSMContext):

    await state.update_data(weight = message.text)
    await bot.send_message(message.from_user.id, """Пришлите вашу активность если
    1) 1,2 – минимальная активность (сидячий образ жизни)

    2) 1,375 – лёгкая активность (1-3 тренировки в неделю)

    3) 1,55 – умеренная активность (3-5 тренировок)

    4) 1,725 – высокая активность (6-7 тренировок + физическая работа)

    5) 1,9 – экстремальная активность (профессиональные спортсмены)""", reply_markup=kebn())
    await state.set_state(CBGU.act)


@user_router.message(CBGU.act)
async def change_day6(message: types.Message, state:FSMContext):
    await state.update_data(act = message.text)
    data = await state.get_data()

    BMR = 0
    if data['sex'].lower() == 'м':
        BMR = (10 * int(data['weight'])) + (6.25 * int(data['hight'])) - (5 * int(data['age'])) + 5

    elif data['sex'].lower() == 'ж':
        BMR = (10 * int(data['weight'])) + (6.25 * int(data['hight'])) - (5 * int(data['age'])) - 161
    
    CHK = 0
    if int(data['act']) == 1:
        CHK = BMR * 1.2
    elif int(data['act']) == 2:
        CHK = BMR * 1.375
    elif int(data['act']) == 3:
        CHK = BMR * 1.55
    elif int(data['act']) == 4:
        CHK = BMR * 1.725
    elif int(data['act']) == 5:
        CHK = BMR * 1.9
    
    await bot.send_message(message.from_user.id, f"Вот ваша суточная норма калорий: {CHK}")
    await state.clear()




@user_router.message(Command("buy_train"))
async def prov_tren(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, "Введите пароль для активации")
    await state.set_state(pokup.code)


@user_router.message(pokup.code)
async def prov_tren1(message: types.Message, state:FSMContext):
    print(message.text)
    if str(message.text) == '1234':
        with open('pay_idd.txt', 'w') as file:
            file.write(str(message.from_user.id)+',')
        await bot.send_message(message.from_user.id, 'Вы активировали тренировки')
    await state.clear()




@user_router.message(Command("train"))
async def prov_tren(message: types.Message, state: FSMContext):
    chel = []
    with open("pay_idd.txt", "r", encoding="utf-8") as file:
        line1 = file.readline()
        chel = line1.split(',')
    if str(message.from_user.id) in chel:
        file_path = 'trenki.txt'
    
    # Создаем объект FSInputFile
        document = FSInputFile(file_path)
    
    # Отправляем документ пользователю
        await bot.send_document(message.from_user.id, document)
    else:
        await bot.send_message(message.from_user.id, "Вы не купили тренировки")




@user_router.message(Command("team"))
async def prov_tren(message: types.Message, state: FSMContext):
    textt = """Наша команда:
1) Михаил Рубцов - программист
2) Тепляков Кирилл - дизайнер интерфейса
3) Видюдин Арсений - team leader
4) Архипов Александр - тестировщик"""
    await bot.send_message(message.from_user.id, textt)
    


@user_router.message(Command("donat"))
async def prov_tren(message: types.Message, state: FSMContext):
    textt = """Если хотите поддержать то присылайте  деньги сюда:
2343 2343 3242 2343"""
    await bot.send_message(message.from_user.id, textt)