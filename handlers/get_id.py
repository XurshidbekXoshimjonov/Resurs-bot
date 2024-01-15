from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu
from loader import bot


get_id_router: Router = Router()


@get_id_router.message()
async def get_id_handler(msg: Message):
    file_id = msg.document.file_id
    await msg.reply(file_id)


