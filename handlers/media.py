from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import  media
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

media_router: Router = Router()






@media_router.message(F.text == 'Axborot va Media')
async def message(msg: Message):
    await msg.answer("Media dasturlaridan birini yuklab olish uchun tugmalardan birini bosing!", reply_markup=media)

@media_router.message(F.text == 'Adobe Animate')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICrWW-E1Id3jpBG2PviKOfKwO5HWGYAALgPwACMJqBSZzB4QzBElj4NAQ", caption="Marhamat Animate dasturini yuklab oling!😉")

@media_router.message(F.text == 'Adobe Media Encover')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICr2W-E4bt5fd5f8qOcV4NLcZ_Y_OBAAL0PgACMJqBSWjhQ9ttAXJyNAQ", caption="Marhamat Media Encover dasturini yuklab oling!😉")




