from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from handlers.keybooards import kebad, kebn, kebv, key_day, key_day_e
from fun_bd import add_sched, watc_sched, del_sched, prov_in, watc_sched_day, add_sched_time, prov_time, prov_dayy, add_time_user, che_rasp_user
import os
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
rasp_router = Router()


# создание класса стате для того чтобы просить у пользователя расписание

class del_rasp(StatesGroup):
    del_ch = State()

class chenge_time(StatesGroup):
    daay = State()
    ttime = State()

class chenge_rasp(StatesGroup):
    daay = State()
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
    mon = State()
    tue = State()
    wed = State()
    thu = State()
    fri = State()
    sat = State()
    sun = State()
    mon_t = State()
    tue_t = State()
    wed_t = State()
    thu_t = State()
    fri_t = State()
    sat_t = State()
    sun_t = State()


#функция для добавления рассписания

@rasp_router.message(Command('add_schedule'))
async def addschedule(message: types.Message, state :FSMContext):
    if not prov_in(int(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в понедельник')
        await state.set_state(train_sched.mon)
    else:
        await bot.send_message(message.from_user.id, 'Ваше рассписание уже есть!', reply_markup=kebn())
        await state.clear()


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
    await bot.send_message(message.from_user.id, 'Вы закончили заполнение расписания! Теперь высмоете его посмотреть, а так же назначить время во сколько вам нужно напоминать на каждый конкретный день.', reply_markup=kebn())
    data = await state.get_data()
    add_sched(int(message.from_user.id),data['mon'],data['tue'],data['wed'],data['thu'],data['fri'],data['sat'],data['sun'])
    await state.clear()
    

    




# функция которая присылает все рассписание пользователю
@rasp_router.message(Command("all_schedule"))
async def help(message: types.Message):
    if prov_in(message.from_user.id) == True:
        a = watc_sched(message.from_user.id)
        await bot.send_message(message.from_user.id, f"""Вот твое расписание:
Понедельник:
{a[2]}

Вторник:
{a[3]}

Среда:
{a[4]}

Четверг:
{a[5]}

Пятница:
{a[6]}

Суббота:
{a[7]}

Воскресенье:
{a[8]}""", reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, 'Вы еще не добавляли расписание.', reply_markup=kebn())

#удаление рассписания
@rasp_router.message(Command("del_schedule"))
async def help(message: types.Message, state: FSMContext):
    if prov_in(message.from_user.id) == True:
        await bot.send_message(message.from_user.id, f'Вы точно хотите удалить расписание? Для удаления напишите да или yes')
        await state.set_state(del_rasp.del_ch)
    else:
        await bot.send_message(message.from_user.id, 'Вам нечего удалять', reply_markup=kebn())
        await state.clear()



@rasp_router.message(del_rasp.del_ch)
async def help(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да' or message.text.lower() == 'yes':
        del_sched(int(message.from_user.id))
        await bot.send_message(message.from_user.id, f'Ваше рассписание успешно удалено', reply_markup=kebn())
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы не подтвердили удаление', reply_markup=kebn())
        await state.clear()


#вызывает клавиатуру с днями недели или говорит что не рассписания
@rasp_router.message(Command("schedule"))
async def help(message: types.Message):
    print(5)
    if prov_in(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Выберите день недели', reply_markup= key_day())
    else:
        await bot.send_message(message.from_user.id, 'Вы еще не добавили свое рассписание', reply_markup= kebn())

@rasp_router.message(Command("Monday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Monday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в понедельник')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())


@rasp_router.message(Command("Tuesday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Tuesday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка во вторник')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())


@rasp_router.message(Command("Wednesday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Wednesday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в среду')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())

@rasp_router.message(Command("Thursday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Thursday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в четверг')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())


@rasp_router.message(Command("Friday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Friday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в пятницу')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())


@rasp_router.message(Command("Saturday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Saturday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в субботу')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())



@rasp_router.message(Command("Sunday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Sunday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в воскресенье')
    await bot.send_message(message.from_user.id, a, reply_markup= kebn())










# добавление рассписания + время


@rasp_router.message(Command('add_schedule_time'))
async def addschedule_time(message: types.Message, state :FSMContext):
    if not prov_in(int(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в понедельник')
        await state.set_state(train_sched_time.mon)
    else:
        await bot.send_message(message.from_user.id, 'Ваше рассписание уже есть', reply_markup=kebn())
        await state.clear()


@rasp_router.message(train_sched_time.mon)
async def mon_tr(message: types.Message, state: FSMContext):
    await state.update_data(mon = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать в понедельник')
    await state.set_state(train_sched_time.mon_t)

@rasp_router.message(train_sched_time.tue)
async def tue_tr(message: types.Message, state: FSMContext):
    await state.update_data(tue = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать во вторник')
    await state.set_state(train_sched_time.tue_t)

@rasp_router.message(train_sched_time.wed)
async def wed_tr(message: types.Message, state: FSMContext):
    await state.update_data(wed = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать в среду')
    await state.set_state(train_sched_time.wed_t)

@rasp_router.message(train_sched_time.thu)
async def thu_tr(message: types.Message, state: FSMContext):
    await state.update_data(thu = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать в четверг')
    await state.set_state(train_sched_time.thu_t)

@rasp_router.message(train_sched_time.fri)
async def fri_tr(message: types.Message, state: FSMContext):
    await state.update_data(fri = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать в пятницу')
    await state.set_state(train_sched_time.fri_t)

@rasp_router.message(train_sched_time.sat)
async def sat_tr(message: types.Message, state: FSMContext):
    await state.update_data(sat = message.text)
    await bot.send_message(message.from_user.id, 'Пришли время во сколько напоминать в субботу')
    await state.set_state(train_sched_time.sat_t)

@rasp_router.message(train_sched_time.sun)
async def sun_tr(message: types.Message, state: FSMContext):
    await state.update_data(sun = message.text)
    await bot.send_message(message.from_user.id, 'Во сколько времени вам напоминать в воскресенье')
    await state.set_state(train_sched_time.sun_t)

# уже начало заполнение времени
@rasp_router.message(train_sched_time.mon_t)
async def mon_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(mon_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки во вторник')
        await state.set_state(train_sched_time.tue)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для понедельника, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.tue_t)
async def tue_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(tue_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в среду')
        await state.set_state(train_sched_time.wed)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для вторника, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.wed_t)
async def wed_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(wed_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в четверг')
        await state.set_state(train_sched_time.thu)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для среды, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.thu_t)
async def thu_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(thu_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в пятницу')
        await state.set_state(train_sched_time.fri)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для четверга, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.fri_t)
async def fri_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(fri_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в субботу')
        await state.set_state(train_sched_time.sat)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для пятницы, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()

@rasp_router.message(train_sched_time.sat_t)
async def sat_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(sat_t = message.text)
        await bot.send_message(message.from_user.id, 'Пришли свои тренировки в воскресенье')
        await state.set_state(train_sched_time.sun)
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для субботы, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()


@rasp_router.message(train_sched_time.sun_t)
async def sun_tr(message: types.Message, state: FSMContext):
    if prov_time(message.text):
        await state.update_data(sun_t = message.text)
        await bot.send_message(message.from_user.id, 'Вы закончили заполнение расписания', reply_markup=kebn())
        data = await state.get_data() # получение всех данных которые ввел пользователь и послудующее добавление в базу данных
        print(data)
        add_sched_time(int(message.from_user.id),data['mon'],data['tue'],data['wed'],data['thu'],data['fri'],data['sat'],data['sun'],data['mon_t'],data['tue_t'],data['wed_t'],data['thu_t'],data['fri_t'],data['sat_t'],data['sun_t'])
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время для воскресенья, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()




# функция по добавлению времени , а так же замене времени в конкретный день
@rasp_router.message(Command("time_change"))
async def add_time(message: types.Message, state: FSMContext):
    if not prov_in(message.from_user.id):
        await bot.send_message(message.from_user.id, 'у вас нет расписания чтобы добавить или изменить время время', reply_markup=kebn())
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
        print(data)
        add_time_user(int(message.from_user.id),data['daay'],data['ttime'])
        await state.clear()
    else:
        await bot.send_message(message.from_user.id, 'Вы ввели некоректное время, повторите попытку заполнения расписания заново без ошибок', reply_markup=kebn())
        await state.clear()
    


@rasp_router.message(Command('change_train'))
async def change_day(message: types.message, state:FSMContext):
    if not prov_in(message.from_user.id):
        await bot.send_message(message.from_user.id, 'У вас нет расписания чтобы изменить тренировку', reply_markup=kebn())
    else:
        await bot.send_message(message.from_user.id, 'Выберете день недели', reply_markup=key_day_e())
        await state.set_state(chenge_rasp.daay)

@rasp_router.message(chenge_rasp.daay)
async def change_day(message: types.message, state:FSMContext):
    if prov_dayy(message.text):
        await state.update_data(daay = message.text)
        await bot.send_message(message.from_user.id, 'Пришлите расписание для этого дня', reply_markup=kebn())
        await state.set_state(chenge_rasp.rasp)
    
    else:
        await bot.send_message(message.from_user.id, 'Вы прислали неправильное название дня недели', reply_markup=kebn())
        await state.clear()


@rasp_router.message(chenge_rasp.rasp)
async def change_day(message: types.message, state:FSMContext):

    await state.update_data(rasp = message.text)
    await bot.send_message(message.from_user.id, 'Вы успешно заменили расписание', reply_markup=kebn())
    data = await state.get_data() # получение всех данных которые ввел пользователь и послудующее добавление в базу данных
    print(data)
    che_rasp_user(int(message.from_user.id),data['daay'],data['rasp'])
    await state.clear()

