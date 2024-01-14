import asyncio
import logging
import sys
import aiogram

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

logging.basicConfig(level=logging.INFO) #логирование, чтобы не пропустить важные сообщения
TOKEN = ""
dp = Dispatcher(bot=Bot) #диспетчер


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    languages = ["Русский", "English"]


# эхобот
# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
