from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu2, table
from loader import bot


send_video_router: Router = Router()

@send_video_router.message(F.text == "O'rnatish videolari")
async def message(msg: Message):
    await msg.answer("O'rnatish videolarini ko'rish uchun istalgan tugmani bosing!", reply_markup=menu2)


@send_video_router.message(F.text == "VS Code o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBr2W7ywEN4_dUaqB7-_VvmRZgIJKkAAJASAACOcngSQV1Tw_rir7fNAQ", caption="Visual Code Studio dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Sublime Text o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBvWW7y5FexPaZxJCRivxFatHD6PumAALxRwACiVjhSepJeeeGhDEhNAQ", caption="Sublime text dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Adobe Photoshop o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAICcGW-CtbD7LgNGwOA8_hp-HyknG55AALSRgACYBfxSU7cuNrkZkPvNAQ", caption="Adobe Photoshop dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Adobe Illustrator o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBQGW7wmZJ1Px7IdjpjaAYKQ-B0JOlAAKaPwACRFLYSeeKesXdqukkNAQ", caption="Adobe Illustrator dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Corel Draw o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBSGW7xDebT4y2irnMOkz_wkzN8KbEAAI-QAACRFLYSYUHi9M4uwHGNAQ", caption="Corel Draw dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Adobe Premiere Pro o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBRmW7xBmfRu9cg-5Zaifw8SPncPafAAI7QAACRFLYSVtR9SFzZpYONAQ", caption="Adobe Premiere Pro dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Adobe Audition o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBRGW7w_yr7o1PhWE0HopBuUtKkEnvAAI3QAACRFLYSfAPDQU7Nd6mNAQ", caption="Adobe Audition dasturini o'rnatish qo'llanmasi!")





@send_video_router.message(F.text == "Adobe After Effects o'rnatish videosi")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIBQmW7w-ZtHBk6cFxyzba8ydEqOo6xAAIyQAACRFLYSZzhblA72dTQNAQ", caption="Adobe Audition dasturini o'rnatish qo'llanmasi!")




@send_video_router.message(F.text == "Bot haqida")
async def send_video_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAIDrmW-Je4389Z6AAHKrJzZ-bHn_QMZogACJEgAAmAX8UncBFdt7kL1jjQE", caption="Botimiz haqida tanishtiruv!", reply_markup=table)