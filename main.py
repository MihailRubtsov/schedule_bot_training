import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os
from datetime import datetime, date
from fun_bd import dat_tren, ism_na_nul, obnul
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
        dday = int(date.today().weekday())  # Порядковый номер дня недели для отправки
        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        
        a = str(moscow_time).split()[1].split('.')[0].split(':')
        chass = int(a[0])  # Часы
        minu = int(a[1])  # Минуты

        if chass <= 3:
            dday = 0 if dday == 6 else dday + 1

        if chass == 0 and minu == 0:
            obnul()  # Обнуление каждый день в 00:00

        data = dat_tren(days[dday], days_t[dday]) # Получение информации по конкретному дню
        print(data)

        for i in data:
            if i[-1] is not None:  # Если есть конкретное время на этот день
                vr = i[-1].split(':')
                chass1 = int(vr[0])  # Часы и минуты для конкретного человека
                minu1 = int(vr[1])
                if chass1 == chass and minu1 == minu:  # Проверка совпадения времени для отправки
                    await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                    ism_na_nul(str(i[0]))  # Изменяем проверку, чтобы второй раз случайно не отправить
            elif chass == 10 and minu == 0:  # Если нет конкретного времени, отправка в 10:00
                await bot.send_message(str(i[0]), f'Вот ваш сегодняшний план тренировок:\n{str(i[1])}')
                ism_na_nul(str(i[0]))  # Проверка, чтобы второй раз не отправить

        await asyncio.sleep(10)  # Увеличен интервал проверки до 10
async def main():
    asyncio.create_task(schedule_otpr())  # Запуск асинхронной задачи
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message'])

if __name__ == "__main__":
    asyncio.run(main())