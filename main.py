import asyncio, logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os
import sys
from multiprocessing import Process
import datetime
from handlers.keybooards import kebad, kebn, kebv
from fun_bd import dat_tren
from handlers.user_router import user_router
from handlers.rasp_router import rasp_router
load_dotenv()

Token = os.getenv('API')

bot = Bot(token=Token)             
dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(rasp_router)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_t = ['Monday_t', 'Tuesday_t', 'Wednesday_t', 'Thursday_t', 'Friday_t', 'Saturday_t', 'Sunday_t']

# настройка автоматического отправления рассписания
async def schedule_otpr():
    while True:
        dday = int(datetime.date.today().weekday())
        a = str(datetime.datetime.now()).split(' ')[1].split(':')# время во время проверки
        chass = int(a[0])
        minu = int(a[1]) 
        data = dat_tren(days[dday], days_t[dday]) # получание информации по конкретному дню
        print(data)
        for i in data:
            print(i)
            if i[-1] != None: # если есть конкретное время на этот день тогда выполняется код
                chass1 = int(i[-1][:2])
                minu1 = int(i[-1][3:])
                if chass1 == chass and minu1 == minu:
                    try:
                        await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                        print(minu)
                    except:
                        print('ошибка айди')
            else: # если нет конкретного времени то отправление только в 10 часов утра
                if chass == 10 and minu == 0:
                    try:
                        await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                        print(minu)
                    except:
                        print('ошибка айди')
        await asyncio.sleep(50)



def work():
    asyncio.run(schedule_otpr()) # функция второго потока для того чтобы работа проверка времени отправки пользователям


async def main():
    proc = Process(target = work)
    proc.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message'])
    proc.join()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())