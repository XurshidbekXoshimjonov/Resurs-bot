from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import menu, table, menu3
from loader import bot
from states.states import Form
from aiogram.fsm.context import FSMContext

menu_router: Router = Router()

@menu_router.message(F.text == 'Dasturlar')
async def message(msg: Message):
    await msg.answer("Bironta bo'limni tanlang!", reply_markup=menu3)








@menu_router.message(Command("help"))
async def start(message: Message):
    await message.answer("Assalomu alaykum sizga qanday yordam bera olaman?\nAgar botda kamchilik yoki noqulaylik sezsangiz Bot admini: @Xoshim0ff ga murojaat qiling!", reply_markup=table)



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

    await bot.send_message(chat_id="5626949720", text=f"Savol va Taklif: {user['addmean']}\n👨‍💻 Murojaatchi: @{message.from_user.username}")



@menu_router.message(F.text == "🔝 Asosiy menu")
async def message(msg: Message):
    await msg.answer("Asosiy menu", reply_markup=table)



@menu_router.message(F.text == "🔙 Orqaga")
async def message(msg: Message):
    await msg.answer("Bo'limni tanlang", reply_markup=menu3)


