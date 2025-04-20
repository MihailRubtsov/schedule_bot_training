from aiogram import Bot, types, Dispatcher, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from handlers.keybooards import kebad, kebn, kebv, key_day_e
from fun_db import *
from .nazv_kom import *
import os
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
rasp_router = Router()


# создание класса стате для того чтобы просить у пользователя расписание

class del_rasp(StatesGroup):
    del_ch = State()


class file_rasp(StatesGroup):
    fileee = State()

class chenge_time(StatesGroup):
    daay = State()
    ttime = State()


class nedel(StatesGroup):
    number = State()

class chenge_rasp(StatesGroup):
    number = State()
    rasp = State()

class train_sched(StatesGroup):
    mon = State()
    tue = State()
    wed = State()
    thu = State()
    fri = State()
    sat = State()
    sun = State()

#  для того чтобы собирать у пользователя расписание со временем
class train_sched_time(StatesGroup):
    mon_t = State()
    tue_t = State()
    wed_t = State()
    thu_t = State()
    fri_t = State()
    sat_t = State()
    sun_t = State()





#функция для добавления рассписания без времени
# @rasp_router.message(Command('add_schedule') or F.text.lower() == b_sched_add)
@rasp_router.message(F.text.lower() == b_sched_add)
async def addschedule(message: types.Message, state :FSMContext):
    if int(kol_nedel(message.from_user.id)) <5:
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в понедельник')
        await state.set_state(train_sched.mon)
    else:
        await bot.send_message(message.from_user.id, 'У вас достигнут лимит в 5 недель')


@rasp_router.message(train_sched.mon)
async def mon_tr(message: types.Message, state: FSMContext):
    await state.update_data(mon = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки во вторник')
    await state.set_state(train_sched.tue)

@rasp_router.message(train_sched.tue)
async def tue_tr(message: types.Message, state: FSMContext):
    await state.update_data(tue = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки в среду')
    await state.set_state(train_sched.wed)

@rasp_router.message(train_sched.wed)
async def wed_tr(message: types.Message, state: FSMContext):
    await state.update_data(wed = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки в четверг')
    await state.set_state(train_sched.thu)

@rasp_router.message(train_sched.thu)
async def thu_tr(message: types.Message, state: FSMContext):
    await state.update_data(thu = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки в пятницу')
    await state.set_state(train_sched.fri)

@rasp_router.message(train_sched.fri)
async def fri_tr(message: types.Message, state: FSMContext):
    await state.update_data(fri = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки в субботу')
    await state.set_state(train_sched.sat)

@rasp_router.message(train_sched.sat)
async def sat_tr(message: types.Message, state: FSMContext):
    await state.update_data(sat = message.text)
    await bot.send_message(message.from_user.id, 'Пришли свои тренировки в воскресенье')
    await state.set_state(train_sched.sun)

@rasp_router.message(train_sched.sun)
async def sun_tr(message: types.Message, state: FSMContext):
    await state.update_data(sun = message.text)
    data = await state.get_data()
    raspis = f"{data['mon']}@#@{data['tue']}@#@{data['wed']}@#@{data['thu']}@#@{data['fri']}@#@{data['sat']}@#@{data['sun']}"
    add_sched(int(message.from_user.id),raspis)
    await bot.send_message(message.from_user.id, 'Вы закончили заполнение расписания!', reply_markup=kebn())
    await state.clear()





# функция которая присылает все рассписание пользователю
# @rasp_router.message(Command("all_schedule") or F.text.lower() == b_all_sched)
@rasp_router.message(F.text.lower() == b_all_sched)
async def help(message: types.Message):
    if kol_nedel(message.from_user.id) != 0:
        a = watc_sched(message.from_user.id)
        await bot.send_message(message.from_user.id, a, reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, 'Вы еще не добавляли расписание.', reply_markup=kebn())

#удаление последней недели
# @rasp_router.message(Command("del_schedule") or F.text.lower() == b_del_week)
@rasp_router.message(F.text.lower() == b_del_week)
async def help(message: types.Message, state: FSMContext):
    if kol_nedel(message.from_user.id) != 0:
        await bot.send_message(message.from_user.id, f'Вы точно хотите удалить расписание? Вы удалите только последнюю неделю. Для удаления напишите да или yes')
        await state.set_state(del_rasp.del_ch)
    else:
        await bot.send_message(message.from_user.id, 'Вам нечего удалять', reply_markup=kebn())
        await state.clear()

@rasp_router.message(del_rasp.del_ch)
async def help(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да' or message.text.lower() == 'yes':
        del_sched(int(message.from_user.id))
        await bot.send_message(message.from_user.id, f'Ваша последняя неделя удалена', reply_markup=kebn())
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы не подтвердили удаление', reply_markup=kebn())
        await state.clear()





# просмотр конкретной недели рассписания
# @rasp_router.message(Command("schedule_ned") or F.text.lower() == b_sched_ned) 
@rasp_router.message(F.text.lower() == b_sched_ned) 
async def help(message: types.Message, state : FSMContext):
    if kol_nedel(message.from_user.id) != 0:
        await bot.send_message(message.from_user.id, f'Пришлите номер недели, которую вы хотите посмотреть. Всего недель у вас {kol_nedel(message.from_user.id)}', reply_markup= kebn())
        await state.set_state(nedel.number)
    else:
        await bot.send_message(message.from_user.id, 'Вы еще не добавили свое рассписание', reply_markup= kebn())

@rasp_router.message(nedel.number)
async def nedel_otpr(message: types.Message, state: FSMContext):
    try:
        if int(message.text) <= int(kol_nedel(message.from_user.id)) and int(message.text) >= 1:
            await bot.send_message(message.from_user.id, watch_ned(message.from_user.id, message.text))
            await state.clear()
        else:
            await bot.send_message(message.from_user.id, 'Вы ввели неправильный номер')
    except:
        await bot.send_message(message.from_user.id, 'Вы ввели неправильный номер')
        await state.clear()





# добавление времени отправки
# @rasp_router.message(Command('add_time') or F.text.lower() == b_time_add)
@rasp_router.message(F.text.lower() == b_time_add)
async def addschedule_time(message: types.Message, state :FSMContext):
    await bot.send_message(message.from_user.id, 'Пришли время отправки в понедельник')
    await state.set_state(train_sched_time.mon_t)

@rasp_router.message(train_sched_time.mon_t)
async def mon_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(mon_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки во вторник')
        await state.set_state(train_sched_time.tue_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для понедельника, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.tue_t)
async def tue_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(tue_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки в среду')
        await state.set_state(train_sched_time.wed_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для вторника, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.wed_t)
async def wed_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(wed_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки в четверг')
        await state.set_state(train_sched_time.thu_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для среды, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.thu_t)
async def thu_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(thu_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки в пятницу')
        await state.set_state(train_sched_time.fri_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для четверга, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.fri_t)
async def fri_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(fri_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки в субботу')
        await state.set_state(train_sched_time.sat_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для пятницы, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.sat_t)
async def sat_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(sat_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли время отправки в воскресенье')
        await state.set_state(train_sched_time.sun_t)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для субботы, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.sun_t)
async def sun_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(sun_t = message.text)
        await bot.send_message(message.from_user.id, 'Вы закончили заполнение расписания', reply_markup=kebn())
        data = await state.get_data() # получение всех данных которые ввел пользователь и послудующее добавление в базу данных
        add_time_p(str(message.from_user.id), data['mon_t'], data['tue_t'], data['wed_t'], data['thu_t'], data['fri_t'], data['sat_t'], data['sun_t'])
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для воскресенья, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()





# функция по добавлению времени на конкретный день , а так же замене времени в конкретный день
# @rasp_router.message(Command("time_change") or F.text.lower() == b_time_change)
@rasp_router.message(F.text.lower() == b_time_change)
async def add_time(message: types.Message, state: FSMContext):
    if kol_nedel(message.from_user.id) == 0:
        await bot.send_message(message.from_user.id, 'у вас нет расписания чтобы изменить время время', reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, 'Выберете день недели', reply_markup=key_day_e())
        await state.set_state(chenge_time.daay)

@rasp_router.message(chenge_time.daay)
async def change_day(message: types.message, state:FSMContext):
    if prov_dayy(message.text):
        await state.update_data(daay = message.text)
        await bot.send_message(message.from_user.id, 'Пришлите время для этого дня', reply_markup=kebn())
        await state.set_state(chenge_time.ttime)
    else:
        await bot.send_message(message.from_user.id, 'Вы прислали не правильное название дня недели', reply_markup=kebn())
        await state.clear()

@rasp_router.message(chenge_time.ttime)
async def change_day(message: types.message, state:FSMContext):
    if prov_time(message.text):
        await state.update_data(ttime = message.text)
        await bot.send_message(message.from_user.id, 'Вы успешно заменили время', reply_markup=kebn())
        data = await state.get_data() # получение всех данных которые ввел пользователь и послудующее добавление в базу данных
        add_time_user(int(message.from_user.id),data['daay'],data['ttime'])
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()





# Функция которая позволяет заменить тренировку в конкретный день
# @rasp_router.message(Command('change_train') or F.text.lower() == b_change_train)
@rasp_router.message(F.text.lower() == b_change_train)
async def change_day(message: types.message, state:FSMContext):
    if kol_nedel(message.from_user.id) == 0:
        await bot.send_message(message.from_user.id, 'У вас нет расписания чтобы изменить тренировку', reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, f'Пришлите номер недели, всего недель у вас {kol_nedel(message.from_user.id)}, само расписание пришлите файлом по шаблону.', reply_markup=key_day_e())
        await state.set_state(chenge_rasp.number)

@rasp_router.message(chenge_rasp.number)
async def change_day(message: types.message, state:FSMContext):
    try:
        if int(message.text) <= int(kol_nedel(message.from_user.id)) and int(message.text) >= 1:
            await state.update_data(daay = message.text)
            await bot.send_message(message.from_user.id, 'Пришлите файл рассписания для этой недели.', reply_markup=kebn())
            await state.set_state(chenge_rasp.rasp)
    except:
        await bot.send_message(message.from_user.id, 'вы прислали не правильный номер недели')

@rasp_router.message(chenge_rasp.rasp)
async def change_day(message: types.message, state:FSMContext):
    data = await state.get_data() # получение всех данных которые ввел пользователь и послудующее добавление в базу данных
    try:
        if message.document:
            file_id = message.document.file_id
            file_name = f'{message.from_user.id}' + f'{message.from_user.id}' + '.txt'
            file_path = os.path.join(os.getcwd(), file_name)  # Сохраняем файл в текущую директорию
        # Скачиваем файл
            file = await bot.get_file(file_id)
            await bot.download_file(file.file_path, file_path)
            try:
                raspis = work_with_file(file_name)
                che_rasp_user(int(message.from_user.id),data['daay'], raspis)
                await bot.send_message(message.from_user.id, 'Вы успешно заменили расписание', reply_markup=kebn())
                os.remove(file_name)
            except:
                await bot.send_message(message.from_user.id, 'Вы прислали не правильно заполненный файл')
                os.remove(file_name)
    except:
        await bot.send_message(message.from_user.id, 'вы отправили файл не txt разрешения или неправильно оформили файл')
    await state.clear()





# #функция которая добавляет рассписание по файлу
# @rasp_router.message(Command('add_schedule_file') or F.text.lower() == b_add_file)
@rasp_router.message(F.text.lower() == b_add_file)
async def addschedule(message: types.Message, state :FSMContext):
    if int(kol_nedel(message.from_user.id)) == 5:
        await bot.send_message(message.from_user.id, 'у вас достигнут лимит в 5 недель', reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, 'пришли мне свой файл')
        await state.set_state(file_rasp.fileee)


@rasp_router.message(file_rasp.fileee)
async def addschedule(message: types.Message, state :FSMContext):
    try:
        if message.document:
            file_id = message.document.file_id
            file_name = f'{message.from_user.id}' + f'{message.from_user.id}' + '.txt'
            file_path = os.path.join(os.getcwd(), file_name)  # Сохраняем файл в текущую директорию
        # Скачиваем файл
            file = await bot.get_file(file_id)

            await bot.download_file(file.file_path, file_path)

            try:
                raspis = work_with_file(file_name)

                add_sched(int(message.from_user.id),raspis)

                await bot.send_message(message.from_user.id, 'Ваше рассписание успешно добавленно', reply_markup=kebn())

                os.remove(file_name)
            except:
                await bot.send_message(message.from_user.id, 'Вы прислали не правильно заполненный файл')
                os.remove(file_name)
    except:
        await bot.send_message(message.from_user.id, 'вы отправили файл не txt разрешения или неправильно оформили файл')