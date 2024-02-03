from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu2, table
from loader import bot


dars_router: Router = Router()

@dars_router.message(F.text == "Darslarimiz")
async def dars_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAICbGW-Ce7IX3TGSRUoy9LHF2UtAbnjAAK4PgACZofwSUN2AAEIpVyDEjQE", caption="Darsimizdan lavha!\nKanal linki: https://t.me/+fkx4FiyVsQg5YTcy", reply_markup=table)