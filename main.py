import asyncio
import logging
import os
from datetime import datetime
import pytz
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from fun_db import (
    day_now, obn_ned, obnul, get_data, get_train_day, ism_na_nul
)
from handlers.user_router import user_router
from handlers.rasp_router import rasp_router
from handlers.admin_router import admin_router

# Логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    filename=os.path.join("logs", "bot_log.txt"),
    filemode="a",
    encoding="utf-8"
)
logger = logging.getLogger("scheduler")

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("API")

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(rasp_router)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_t = ['Monday_t', 'Tuesday_t', 'Wednesday_t', 'Thursday_t', 'Friday_t', 'Saturday_t', 'Sunday_t']


async def schedule_tick():
    """Один проход проверки времени и отправки сообщений"""
    pr = True
    dday = day_now()
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    chass = moscow_time.hour
    minu = moscow_time.minute

    if chass <= 3:
        dday = 0 if dday == 6 else dday + 1

    # Обнуление в 00:00
    if chass == 0 and minu == 0:
        if dday == 0:
            if pr:
                obn_ned()
                pr = False
            obnul()
            await bot.send_message('1120554354', 'Произошёл переход на новую неделю')
        else:
            obnul()
            await bot.send_message('1120554354', 'Произошел переход на новый день')
    else:
        if pr is False:
            pr = True
        data = get_data()
        for i in data:
            if i[-1] == 1 and i[2] != 0:
                vr = i[4 + dday].split(':')
                chass1 = int(vr[0])
                minu1 = int(vr[1])
                if chass1 == chass and minu1 == minu:
                    rasp = get_train_day(i[1], i[3], dday)
                    try:
                        await bot.send_message(
                            str(i[1]),
                            f'Вот ваш сегодняшний план тренировок\n\n'
                            f'Неделя номер {i[3]}\n\n'
                            f'День: {days[dday]}\n\n{str(rasp)}'
                        )
                        ism_na_nul(str(i[1]))
                    except Exception:
                        logger.exception(f"Ошибка при отправке пользователю {i[1]}")


async def schedule_runner():
    """Вечный цикл, с перезапуском каждые 2 дня"""
    start_time = datetime.now()
    while True:
        try:
            await schedule_tick()
        except asyncio.CancelledError:
            logger.info("Фоновая задача остановлена")
            raise
        except Exception:
            logger.exception("Ошибка в schedule_tick()")
            await asyncio.sleep(5)  # пауза перед повтором

        # Проверка на 48 часов работы
        elapsed = (datetime.now() - start_time).total_seconds()
        if elapsed >= 172800:  # 48 часов
            logger.info("Перезапуск фоновой задачи (прошло 2 дня)")
            start_time = datetime.now()  # сбрасываем время
            break

        await asyncio.sleep(10)


async def schedule_manager():
    """Менеджер, который перезапускает schedule_runner каждые 2 дня"""
    while True:
        await schedule_runner()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    bg_task = asyncio.create_task(schedule_manager(), name="schedule_manager")
    try:
        await dp.start_polling(bot, allowed_updates=['message'])
    finally:
        bg_task.cancel()
        try:
            await bg_task
        except asyncio.CancelledError:
            pass
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
