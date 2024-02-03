from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import  grafik_dizayn
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

grafik_dizayn_router: Router = Router()


@grafik_dizayn_router.message(F.text == 'Grafik dizayn')
async def message(msg: Message):
    await msg.answer("Grafik dizayn dasturlaridan birini yuklab olish uchun tugmalardan birini bosing!", reply_markup=grafik_dizayn)

@grafik_dizayn_router.message(F.text == 'Adobe Photoshop')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICpWW-DlV64zx9EwwKIMY7pk_sl423AAJ1PwACMJqBSd3ab-kMXrgfNAQ", caption="Marhamat Photoshop dasturini yuklab oling!😉")

@grafik_dizayn_router.message(F.text == 'Adobe Illustrator')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICiGW-C8_4WEXoTiVEbuRXJqvA3PgRAAKkPwACMJqBSV0XCVY8cxAyNAQ", caption="Marhamat Illustrator dasturini yuklab oling!😉")

@grafik_dizayn_router.message(F.text == 'Corel Draw')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICoWW-DUY9s_--vUjGXHVzO2StEZtjAAJLJwAC0-z4S-yN2dwyMW94NAQ", caption="Marhamat Corel Draw dasturini yuklab oling!😉")

@grafik_dizayn_router.message(F.text == 'Adobe Photoshop Lightroom')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICqWW-EAE8dy9m6Vd1yd5bBzFsgsKwAAJ5OgACCxG4Sfp7DtOX5_fKNAQ", caption="Marhamat Lightroom dasturini yuklab oling!😉")
