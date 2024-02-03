from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import video_montaj
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

video_montaj_router: Router = Router()





@video_montaj_router.message(F.text == 'Video montaj')
async def message(msg: Message):
    await msg.answer("Video montaj dasturlaridan birini yuklab olish uchun tugmalardan birini bosing!", reply_markup=video_montaj)

@video_montaj_router.message(F.text == 'Adobe Premiere Pro')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICjGW-DAJ7JZx72AaqjrOByeL8VbcZAALiPgACMJqBSW00zqzGKdB_NAQ", caption="Marhamat Premiere Pro dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'Adobe Audition')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICjmW-DEsvpBcc9uIlFiO4PQ6EG9Y-AALuQAACMJqJSSqoPmZUhuLSNAQ", caption="Marhamat Audition dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'Adobe After Effects')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICimW-C-2O7xIYMSLnTNr5V6K8hS7xAAI1PwACMJqBSc7tXbuF8EyUNAQ", caption="Marhamat After Effects dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'VFX Suite')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICtWW-FU5N10_FxAjzk3BHij99NjEzAAJqIQACI6iZSn2ivtGSGJDoNAQ", caption="Marhamat VFX dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'Universe')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICt2W-FYMnZAzY4o5oWc0bjvB6InGWAAJnIQACI6iZSoK1zqKx_NCjNAQ", caption="Marhamat Universe dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'TrapCode Suite')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICuWW-FbW0r5MlxJJIxBiBNHxbBWsLAAJeIQACI6iZSj-LDHGCxPXFNAQ", caption="Marhamat TrapCode dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'DaVinci')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICu2W-FjHMwXR4bf9LUcJ3wy8j9H4bAAIEHgAC3mXJSeoRMxQ_SBZPNAQ", caption="Marhamat DaVinci dasturini yuklab oling!😉")

@video_montaj_router.message(F.text == 'Screen Recorder')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAICp2W-D6QsaK6Q87p2RZkFT_DQX6juAAIZRwACYBfxST0TPlxSuqnMNAQ", caption="Marhamat Screen Recorder dasturini yuklab oling!😉")
