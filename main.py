from aiogram.types import Message, CallbackQuery
from aiogram import executor
from config import dp, bot
from reply import menuStart
from inline import *
from ballar import *
import logging


@dp.message_handler(commands='start')
async def start(message: Message):
    txt = f"Assalomu-alaykum {message.from_user.full_name}!\nVKey Music Botiga hush kelibsiz"
    await message.answer_photo(open("image/logo.jpg", "rb"), txt, reply_markup=menuStart)


@dp.message_handler(commands='help')
async def hlp(message: Message):
    txt = f"Yordam uchun biz bilan bog'lanishingiz mumkin!"
    await message.answer_photo(open("image/help.jpg", "rb"), txt, reply_markup=boglan)

@dp.callback_query_handler(text_contains="boglanish")
async def helpcom(call: CallbackQuery):
    await call.message.answer_photo(open("image/logo.jpg", "rb"),
                                    caption="💬Ijtimoiy tarmoqlarda bizning manzillarimiz:", reply_markup=admin_btn)
    await call.answer(cache_time=60)


@dp.message_handler(text="Programming")
async def prog(message: Message):
    txt = "1-savol"
    await message.answer(txt, reply_markup=sav0)


@dp.callback_query_handler()
async def funk(call: CallbackQuery):
    if call.data == "k0":
        await call.message.delete()
        await call.message.answer("1-savol", reply_markup=sav0)
        await call.answer(cache_time=60)
    elif call.data == "k1":
        await call.message.delete()
        await call.message.answer("2-savol", reply_markup=sav1)
        await call.answer(cache_time=60)
    elif call.data == "k2":
        await call.message.delete()
        await call.message.answer("3-savol", reply_markup=sav2)
        await call.answer(cache_time=60)
    elif call.data == "k3":
        await call.message.delete()
        await call.message.answer("4-savol", reply_markup=sav3)
        await call.answer(cache_time=60)
    elif call.data == "k4":
        await call.message.delete()
        await call.message.answer("5-savol", reply_markup=sav4)
        await call.answer(cache_time=60)
    elif call.data == "k5":
        await call.message.delete()
        await call.message.answer("6-savol", reply_markup=sav5)
        await call.answer(cache_time=60)
    elif call.data == "k6":
        await call.message.delete()
        await call.message.answer("7-savol", reply_markup=sav6)
        await call.answer(cache_time=60)
    elif call.data == "k7":
        await call.message.delete()
        await call.message.answer("8-savol", reply_markup=sav7)
        await call.answer(cache_time=60)
    elif call.data == "k8":
        await call.message.delete()
        await call.message.answer("9-savol", reply_markup=sav8)
        await call.answer(cache_time=60)
    elif call.data == "k9":
        await call.message.delete()
        await call.message.answer("10-savol", reply_markup=sav9)
        await call.answer(cache_time=60)
    elif call.data == "k10":
        await call.message.delete()
        await call.message.answer("11-savol", reply_markup=sav10)
        await call.answer(cache_time=60)
    elif call.data == "k11":
        await call.message.delete()
        await call.message.answer("12-savol", reply_markup=sav11)
        await call.answer(cache_time=60)
    elif call.data == "k12":
        await call.message.delete()
        await call.message.answer("13-savol", reply_markup=sav12)
        await call.answer(cache_time=60)
    elif call.data == "k13":
        await call.message.delete()
        await call.message.answer("14-savol", reply_markup=sav13)
        await call.answer(cache_time=60)
    elif call.data == "k14":
        await call.message.delete()
        await call.message.answer("15-savol", reply_markup=sav14)
        await call.answer(cache_time=60)
    elif call.data == "k15":
        await call.message.delete()
        await call.message.answer("16-savol", reply_markup=sav15)
        await call.answer(cache_time=60)
    elif call.data == "k16":
        await call.message.delete()
        await call.message.answer("17-savol", reply_markup=sav16)
        await call.answer(cache_time=60)
    elif call.data == "k17":
        await call.message.delete()
        await call.message.answer("18-savol", reply_markup=sav17)
        await call.answer(cache_time=60)
    elif call.data == "k18":
        await call.message.delete()
        await call.message.answer("19-savol", reply_markup=sav18)
        await call.answer(cache_time=60)
    elif call.data == "k19":
        await call.message.delete()
        await call.message.answer("20-savol", reply_markup=sav19)
        await call.answer(cache_time=60)
    elif call.data == "score":
        await call.message.delete()
        await call.message.answer(f"{Ans.summa} ball", reply_markup=menuStart)
        await call.answer(cache_time=60)
        Ans.summa = 0
    elif call.data == "1":
        a = Ans()

@dp.message_handler(text="Kitoblar")
async def book(message: Message):
    await message.answer_document(open("books/Ch5.pdf", "rb"), caption="Chapter 5")
    await message.answer_document(open("books/Ch6.pdf", "rb"), caption="Chapter 5")
    await message.answer_document(open("books/Ch7.pdf", "rb"), caption="Chapter 5")
    await message.answer_document(open("books/Ch8.pdf", "rb"), caption="Chapter 5")
    await message.answer_document(open("books/Ch8_2.pdf", "rb"), caption="Chapter 5")
    await message.answer_document(open("books/Ch11.pdf", "rb"), caption="Chapter 5")


if __name__ == '__main__':
    executor.start_polling(dp)