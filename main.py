import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from datetime import datetime, date
from fun_db import *
import pytz
from handlers.user_router import user_router
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

async def schedule_otpr():
    while True:
        dday = day_now() # Порядковый номер дня недели для отправки
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        a = str(moscow_time).split()[1].split('.')[0].split(':')
        chass = int(a[0])  # Часы
        if chass <= 3:
            dday = 0 if dday == 6 else dday + 1
        minu = int(a[1])  # Минуты
        
        
        if chass == 0 and minu == 0:
            if dday == 0:
                obn_ned()
                obnul()
                await bot.send_message('1120554354', f'произошёл переход на новую неделю')
            else:
                obnul()
                await bot.send_message('1120554354', f'произошел переход на новый день')
        else:
            data = get_data()
            for i in data:
                print(i)
                if i[-1] == 1 and i[2] != 0:
                    vr = i[4 + dday].split(':')
                    chass1 = int(vr[0])  # Часы и минуты для конкретного человека
                    minu1 = int(vr[1])
                    if chass1 == chass and minu1 == minu:
                        rasp = get_train_day(i[1], i[3], dday)
                        await bot.send_message(str(i[1]), f'Вот ваш сегодняшний план тренировок , неделя номер {i[4]}:\n{str(rasp)}')
                        ism_na_nul(str(i[1])) 

        await asyncio.sleep(10) 


        # await asyncio.sleep(10)  # Увеличен интервал проверки до 10
async def main():
    asyncio.create_task(schedule_otpr())  # Запуск асинхронной задачи
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message'])

if __name__ == "__main__":
    asyncio.run(main())