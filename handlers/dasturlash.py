from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, table, menu3
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext


dasturlash_router: Router = Router()

@dasturlash_router.message(F.text == 'Dasturlash')
async def message(msg: Message):
    await msg.answer("Dasturlash dasturlaridan birini yuklab olish uchun tugmalardan birini bosing!", reply_markup=menu)


@dasturlash_router.message(F.text == 'Visual Code Studio')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAMVZaVOKw7lmViSN0scjKFInk_bl3oAAoEnAAKiQmFKxCTycHPDNms0BA", caption="Marhamat VS Code dasturini yuklab oling!😉")

@dasturlash_router.message(F.text == 'Sublime Text')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICo2W-Dh182XC2J0oV6N4WaFQHTKSwAAL8RgACYBfxSbn_ZPiciPj1NAQ", caption="Marhamat Sublime Text dasturini yuklab oling!😉")

@dasturlash_router.message(F.text == 'PyCharm')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICq2W-ElV8nO_6MywkJ_GI8_qRx71PAAIqRwACYBfxSTxKE01NeW01NAQ", caption="Marhamat PyCharm dasturini yuklab oling!😉")