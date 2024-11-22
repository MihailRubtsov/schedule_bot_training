from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv, key_day
from dotenv import load_dotenv
from fun_bd import obnul
import os
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
admin_router = Router()


@admin_router.message(Command("admin"))
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, f"""пока что находится в разработке""", reply_markup=kebn())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')