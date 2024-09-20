import asyncio, logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os
import sys
from multiprocessing import Process
import datetime
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


async def schedule_otpr():
    while True:
        a = datetime.datetime.now()
        dday = int(datetime.date.today().weekday())
        a = str(a).split(' ')[1].split(':')
        minu = int(a[1])
        if minu == 0:
            data = dat_tren(days[dday])
            for i in data:
                try:
                    await bot.send_message(f'Вот ваш сегодняшний план тренировок:\n{str(i[0])}', str(i[1]))
                except:
                    print('ошибка айди')
        await asyncio.sleep(60)


def work():
    asyncio.run(schedule_otpr())


async def main():
    proc = Process(target = work)
    proc.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=['message'])
    proc.join()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())