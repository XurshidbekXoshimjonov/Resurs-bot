from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

menu_router: Router = Router()


@menu_router.message(F.text == 'Visual Code Studio')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAMVZaVOKw7lmViSN0scjKFInk_bl3oAAoEnAAKiQmFKxCTycHPDNms0BA", caption="Marhamat VS Code dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Sublime Text')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMXZaVOUhO4U5KzGchR1C2FR-t_xI0AAiQHAAKw2KBRrnwissLDpCc0BA", caption="Marhamat Sublime Text dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Adobe Photoshop')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMLZaVMYZrhpPl9gTfL293i3zkAAZPFAAI2CAACsX_wUO1522bZd4ixNAQ", caption="Marhamat Photoshop dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Adobe Illustrator')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMNZaVNFIK8nWn5jzPEjWetWmMWwU8AAjQIAAKxf_BQEVrJLWtX6700BA", caption="Marhamat Illutrator dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Corel Draw')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgIAAxkBAAMZZaVOfPLAODt_TAG-a0eCmCjjEwADlDgAAuf_IEiGC8RF8yQkSjQE", caption="Marhamat Corel Draw dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Adobe Premiere Pro')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMPZaVNPQH6bFLtEbokwY-XEmccWo0AAjcIAAKxf_BQWhgtT4EHa3Q0BA", caption="Marhamat Premiere Pro dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Adobe Audition')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMTZaVN46Tr1iIeivZqZn5xL93xoj0AAk0IAAKxf_BQFw8AAWGV6lhWNAQ", caption="Marhamat Audition dasturini yuklab oling!😉")





@menu_router.message(F.text == 'Adobe After Effects')
async def send_file_handler(msg: Message):
    await msg.answer_document("BQACAgQAAxkBAAMRZaVNbKsr0T8II5hIVPyX0j8cuZ8AAkcIAAKxf_BQlH31p_62wxc0BA", caption="Marhamat After Effects dasturini yuklab oling!😉")



@menu_router.message(Command("help"))
async def start(message: Message):
    await message.answer("Assalomu alaykum sizga qanday yordam bera olaman?\nAgar botda kamchilik yoki noqulaylik sezsangiz Bot admini @Xoshim0ff ga murojaat qiling!", reply_markup=menu)



@menu_router.message(Command("admin"))
async def f1(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum siz admin bilan bog'lanish tugmasini bosdingiz!")
    await state.set_state(Form.addmean)
    await message.answer("✏️ Savol yoki takliflaringiz bo'lsa shu yerga yuboring\nSavol yoki takliflaringiz IT resurslar botining adminstrator profiliga yuboriladi!")

@menu_router.message(Form.addmean)
async def  f1(message: Message, state: FSMContext):
    await state.update_data(addmean=message.text)    
    user = await state.get_data()
    await state.clear()
  

    await message.answer(f"Savol va Taklif: {user['addmean']}\n 👨‍💻 Murojaatchi: @{message.from_user.username}", reply_markup=menu)

    await bot.send_message(chat_id="5626949720", text=f"Savol va Taklif: {user['addmean']}\n👨‍💻 Murojaatchi: @{message.from_user.username}")