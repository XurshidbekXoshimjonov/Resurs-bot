from aiogram import Router,F
from aiogram.types import Message,CallbackQuery
from aiogram.methods.get_chat_member import GetChatMember
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import majburiy_obuna, menu, table
from loader import bot
start_router: Router = Router()





@start_router.message(Command("start"))
async def start(message: Message):
    await message.answer("Assalomu alaykum xush kelibsiz!😊")
    await message.answer("Avval kanalimizga obuna bo'ling shundagina botdan to'liq foydalana olasiz!😉", reply_markup=majburiy_obuna)





@start_router.callback_query(F.data=="tasdiqlash")
async def check(query: CallbackQuery):
    user = await GetChatMember(chat_id='-1001864241545', user_id=query.from_user.id)
    
    if user.status == "creator" :
        await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz!\nDasturlardan birini yuklab olish uchun tugmalardan birini bosing!",reply_markup=table)
    elif user.status == "admin":
         await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz!\nDasturlardan birini yuklab olish uchun tugmalardan birini bosing!",reply_markup=table)

    elif user.status == "member":
         await bot.send_message(chat_id=query.from_user.id, text="Kanalga obuna bo'ldingiz, endi botdan foydalana olasiz!\nDasturlardan birini yuklab olish uchun tugmalardan birini bosing!",reply_markup=table)
    else : 
        await bot.send_message(chat_id=query.from_user.id, text="Kechirasiz, agar siz kanalga obuna bo'lmagan bo'lsangiz botdan to'liq foydalana olmaysiz!")
