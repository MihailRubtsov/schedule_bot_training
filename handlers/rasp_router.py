from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from handlers.keybooards import rep_keb_n
from handlers.keybooards import key_day
from fun_bd import add_sched, watc_sched, del_sched, prov_in, watc_sched_day
import os
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
rasp_router = Router()

class train_sched(StatesGroup):
    mon = State()
    tue = State()
    wed = State()
    thu = State()
    fri = State()
    sat = State()
    sun = State()



#функция для добавления рассписания

@rasp_router.message(Command('addschedule'))
async def addschedule(message: types.Message, state :FSMContext):
    if not prov_in(int(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Пришли твои тренировки в понедельник')
        await state.set_state(train_sched.mon)
    else:
        await bot.send_message(message.from_user.id, 'ваше рассписание уже есть')
        await state.clear()


@rasp_router.message(train_sched.mon)
async def mon_tr(message: types.Message, state: FSMContext):
    await state.update_data(mon = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки во вторник')
    await state.set_state(train_sched.tue)

@rasp_router.message(train_sched.tue)
async def tue_tr(message: types.Message, state: FSMContext):
    await state.update_data(tue = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в среду')
    await state.set_state(train_sched.wed)

@rasp_router.message(train_sched.wed)
async def wed_tr(message: types.Message, state: FSMContext):
    await state.update_data(wed = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в четверг')
    await state.set_state(train_sched.thu)

@rasp_router.message(train_sched.thu)
async def thu_tr(message: types.Message, state: FSMContext):
    await state.update_data(thu = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в пятницу')
    await state.set_state(train_sched.fri)

@rasp_router.message(train_sched.fri)
async def fri_tr(message: types.Message, state: FSMContext):
    await state.update_data(fri = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в субботу')
    await state.set_state(train_sched.sat)

@rasp_router.message(train_sched.sat)
async def sat_tr(message: types.Message, state: FSMContext):
    await state.update_data(sat = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в воскресенье')
    await state.set_state(train_sched.sun)

@rasp_router.message(train_sched.sun)
async def sun_tr(message: types.Message, state: FSMContext):
    await state.update_data(sun = message.text)
    await bot.send_message(message.from_user.id, 'вы закончили заполнение')
    data = await state.get_data()
    add_sched(int(message.from_user.id),data['mon'],data['tue'],data['wed'],data['thu'],data['fri'],data['sat'],data['sun'])
    await state.clear()
    

    







@rasp_router.message(Command("allschedule"))
async def help(message: types.Message):
    if prov_in(message.from_user.id) == True:
        a = watc_sched(message.from_user.id)
        await bot.send_message(message.from_user.id, f'вот твое расписание: {a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{a[7]},{a[8]}')
    else:
        await bot.send_message(message.from_user.id, 'вы еще не добавляли расписание')


@rasp_router.message(Command("delschedule"))
async def help(message: types.Message):
    if prov_in(message.from_user.id) == True:
        del_sched(int(message.from_user.id))
        await bot.send_message(message.from_user.id, f'Ваше рассписание успешно удалено')
    else:
        await bot.send_message(message.from_user.id, 'Вам нечего удалять')











@rasp_router.message(Command("schedule"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'расписание', reply_markup= key_day())


@rasp_router.message(Command("Monday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Monday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в понедельник')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())


@rasp_router.message(Command("Tuesday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Tuesday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка во вторник')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())


@rasp_router.message(Command("Wednesday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Wednasday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в среду')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())

@rasp_router.message(Command("Thursday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Thursday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в четверг')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())


@rasp_router.message(Command("Friday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Friday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в пятницу')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())


@rasp_router.message(Command("Saturday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Saturday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в субботу')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())



@rasp_router.message(Command("Sunday"))
async def help(message: types.Message):
    a = watc_sched_day(message.from_user.id, 'Sunday')
    await bot.send_message(message.from_user.id, 'Ваша тренировка в воскресенье')
    await bot.send_message(message.from_user.id, a, reply_markup= rep_keb_n())


