from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import dasturlar
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext


dasturlar_router: Router = Router()

@dasturlar_router.message(F.text == 'Boshqa dasturlar')
async def message(msg: Message):
    await msg.answer("Dasturlardan birini yuklab olish uchun tugmalardan birini bosing!", reply_markup=dasturlar)


@dasturlar_router.message(F.text == 'Adobe InDesign')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICsWW-E-oVpA_YGdLASro_rO1JlegbAAJ2OAACUgdgSUiAG5IBTT-CNAQ", caption="Marhamat InDesign dasturini yuklab oling!😉")


@dasturlar_router.message(F.text == 'Adobe InCopy')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICs2W-FNFtkXCJPx9OzmXDQdCEVJRNAALoKAACKDhQSYhfGSrfIf7YNAQ", caption="Marhamat InCopy dasturini yuklab oling!😉")