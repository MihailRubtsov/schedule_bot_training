import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from multiprocessing import Process
from datetime import datetime, date
from fun_bd import dat_tren
from handlers.user_router import user_router
from fun_bd import ism_na_nul, obnul
import pytz
from handlers.rasp_router import rasp_router
from handlers.admin_router import admin_router
load_dotenv()

Token = os.getenv('API')

bot = Bot(token=Token)             
dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(rasp_router)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_t = ['Monday_t', 'Tuesday_t', 'Wednesday_t', 'Thursday_t', 'Friday_t', 'Saturday_t', 'Sunday_t']

# настройка автоматического отправления рассписания
async def schedule_otpr():
    while True:
        dday = int(date.today().weekday()) # порядковый номер дня недели для отправки
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        a = str(moscow_time).split()[1].split('.')[0].split(':')
        chass = int(a[0]) # часы
        minu = int(a[1]) #минуты
        sec = int(a[2])
        if chass <= 3:
            if dday == 6:
                dday = 0
            else:
                dday += 1
        #if (sec == 15 or sec == 30 or sec == 45 or sec == 0):
        #    await bot.send_message('1120554354', f'{dday, chass, minu}')
        if chass == 0 and minu == 0:
            obnul() # обнуление каждый день в 0:0
        data = dat_tren(days[dday], days_t[dday]) # получание информации по конкретному дню
        #if (sec == 15 or sec == 30 or sec == 45 or sec == 0):
        #    await bot.send_message('1120554354', f'{len(data)}')
        for i in data:
            if i[-1] != None: # если есть конкретное время на этот день тогда выполняется код
                vr = i[-1].split(':')
                chass1 = int(vr[0]) # часы и минуты для конкретного человека
                minu1 = int(vr[1])
                if chass1 == chass and minu1 == minu: # проверка совпадения вермени для отправки
                    await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                    ism_na_nul(str(i[0])) # изменяем проверку чтобы второй раз случайно не отправить
            else: # если нет конкретного времени то отправление только в 10 часов утра
                if chass == 10 and minu == 0:
                    await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                    ism_na_nul(str(i[0])) # проверка чтобы второй раз не отправить
        await asyncio.sleep(1)



def work():
    asyncio.run(schedule_otpr()) # функция второго потока для того чтобы работа проверка времени отправки пользователям


async def main():
    proc = Process(target = work)
    proc.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message'])
    proc.join()


if __name__ == "__main__":
    asyncio.run(main())