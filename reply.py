from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Programming"),
            KeyboardButton(text="Kitoblar"),
        ],
    ],
    resize_keyboard=True
)