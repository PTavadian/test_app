from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor 
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from dotenv import load_dotenv, find_dotenv

storage=MemoryStorage()

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN')) 
dp = Dispatcher(bot, storage=storage) 



@dp.message_handler(content_types=['start'])
async def det_voice(message: types.Message):
    await bot.send_message(message.from_user.id, 'start')


    
@dp.message_handler()
async def det_voice(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)





executor.start_polling(dp, skip_updates=True) 

