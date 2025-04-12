from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv, key_day, key_day_e
from dotenv import load_dotenv
from fun_bd import obnul
from aiogram.fsm.state import State, StatesGroup
import os
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
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
4) /change_train вы можете изменить тренировку в конкретный день
                           
2. /watch_schedule вызывает клавиатуру для просмотра всего расписания а так же его удаления, она имеет в себе такие функции:
1) /all_schedule бот присылает полный тренировочный план
2) /del_schedule вы можете удалить расписание и заполнить заново
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


# CBGU

@user_router.message(Command('raschot'))
async def change_day(message: types.message, state:FSMContext):
    await bot.send_message(message.from_user.id, 'какой у вас пол 1 = м, 2 = ж', reply_markup=key_day_e())
    await state.set_state(CBGU.sex)

@user_router.message(CBGU.sex)
async def change_day(message: types.message, state:FSMContext):

    await state.update_data(sex = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш возраст', reply_markup=kebn())
    await state.set_state(CBGU.age)

@user_router.message(CBGU.age)
async def change_day(message: types.message, state:FSMContext):

    await state.update_data(age = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш рост', reply_markup=kebn())
    await state.set_state(CBGU.hight)


@user_router.message(CBGU.hight)
async def change_day(message: types.message, state:FSMContext):

    await state.update_data(hight = message.text)
    await bot.send_message(message.from_user.id, 'Пришлите ваш вес', reply_markup=kebn())
    await state.set_state(CBGU.weight)


@user_router.message(CBGU.weight)
async def change_day(message: types.message, state:FSMContext):

    await state.update_data(weight = message.text)
    await bot.send_message(message.from_user.id, """Пришлите вашу активность если
    1) 1,2 – минимальная активность (сидячий образ жизни)

    2) 1,375 – лёгкая активность (1-3 тренировки в неделю)

    3) 1,55 – умеренная активность (3-5 тренировок)

    4) 1,725 – высокая активность (6-7 тренировок + физическая работа)

    5) 1,9 – экстремальная активность (профессиональные спортсмены)""", reply_markup=kebn())
    await state.set_state(CBGU.act)


@user_router.message(CBGU.act)
async def change_day(message: types.message, state:FSMContext):
    await state.update_data(act = message.text)
    data = await state.get_data()

    BMR = 0
    if int(data['sex']) == 1:
        BMR = (10 * int(data['weight'])) + (6.25 * int(data['hight'])) - (5 * int(data['age'])) + 5

    elif data['sex'] ==2:
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
    
    await bot.send_message(message.from_user.id, f"Вот ваша суточная норма каллорий: {CHK}")
    await state.clear()


