from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from handlers.keybooards import rep_keb_n
from handlers.keybooards import key_day
from fun_bd import add_sched, watc_sched, del_sched
import sys
import sqlite3
import os
import sys
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



@rasp_router.message(Command('addschedule'))
async def addschedule(message: types.Message, state :FSMContext):
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 1')
    await state.set_state(train_sched.mon)

@rasp_router.message(train_sched.mon)
async def mon_tr(message: types.Message, state: FSMContext):
    await state.update_data(mon = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 2')
    await state.set_state(train_sched.tue)

@rasp_router.message(train_sched.tue)
async def tue_tr(message: types.Message, state: FSMContext):
    await state.update_data(tue = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 3')
    await state.set_state(train_sched.wed)

@rasp_router.message(train_sched.wed)
async def wed_tr(message: types.Message, state: FSMContext):
    await state.update_data(wed = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 4')
    await state.set_state(train_sched.thu)

@rasp_router.message(train_sched.thu)
async def thu_tr(message: types.Message, state: FSMContext):
    await state.update_data(thu = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 5')
    await state.set_state(train_sched.fri)

@rasp_router.message(train_sched.fri)
async def fri_tr(message: types.Message, state: FSMContext):
    await state.update_data(fri = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 6')
    await state.set_state(train_sched.sat)

@rasp_router.message(train_sched.sat)
async def sat_tr(message: types.Message, state: FSMContext):
    await state.update_data(sat = message.text)
    await bot.send_message(message.from_user.id, 'Пришли твои тренировки в 7')
    await state.set_state(train_sched.sun)

@rasp_router.message(train_sched.sun)
async def sun_tr(message: types.Message, state: FSMContext):
    await state.update_data(sun = message.text)
    await bot.send_message(message.from_user.id, 'вы закончили заполнение')
    data = await state.get_data()
    add_sched(int(message.from_user.id),data['mon'],data['tue'],data['wed'],data['thu'],data['fri'],data['sat'],data['sun'])
    print(data)
    await state.clear()
    

    







@rasp_router.message(Command("allschedule"))
async def help(message: types.Message):
    a = watc_sched(int(message.from_user.id))
    print(a)
    await bot.send_message(message.from_user.id, f'вот твое расписание: {a[2]},{a[3]},{a[4]},{a[5]},{a[6]},{a[7]},{a[8]}')


@rasp_router.message(Command("delschedule"))
async def help(message: types.Message):
    del_sched(int(message.from_user.id))
    await bot.send_message(message.from_user.id, f'ваше рассписание успешно удалено')












@rasp_router.message(Command("schedule"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'расписание', reply_markup= key_day())


@rasp_router.message(Command("Monday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())


@rasp_router.message(Command("Tuesday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())


@rasp_router.message(Command("Wednesday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())

@rasp_router.message(Command("Thursday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())


@rasp_router.message(Command("Friday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())


@rasp_router.message(Command("Saturday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())



@rasp_router.message(Command("Sanday"))
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, 'HUI', reply_markup= rep_keb_n())


