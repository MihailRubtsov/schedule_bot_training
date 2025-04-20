from aiogram import Bot, types, Dispatcher, Router 
from aiogram.filters.command import Command
from handlers.keybooards import kebad, kebn, kebv
from dotenv import load_dotenv
import os
from aiogram.types import FSInputFile
load_dotenv()

Token = os.getenv('API')
bot = Bot(token = Token)
admin_router = Router()


@admin_router.message(Command("admin"))
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id, f"""пока что находится в разработке""", reply_markup=kebn())
    with open('all_id.txt', 'w') as file:
        file.write(str(message.from_user.id)+',')




@admin_router.message(Command("sisi_pisi_bom"))
async def command_start(message:types.Message):
    file_path = 'user_train1.db'
    
    # Создаем объект FSInputFile
    document = FSInputFile(file_path)
    await bot.send_document(message.from_user.id, document)


@admin_router.message(Command("sisi_pisi_bom2"))
async def command_start(message:types.Message):
    file_path = 'all_id.txt'
    
    # Создаем объект FSInputFile
    document = FSInputFile(file_path)
    await bot.send_document(message.from_user.id, document)
