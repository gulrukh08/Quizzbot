from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

admin_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/aabdurakhimovaa"),
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/abdulvokhidovna_/")
        ],
    ]
)
boglan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Biz bilan bog'laning", callback_data="boglanish"),
        ]
    ],
)

sav0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="1"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='➡', callback_data="k1")
        ],
    ]
)
sav1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k0"),
            InlineKeyboardButton(text='➡', callback_data="k2"),
        ],
    ]
)
sav2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="1"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k1"),
            InlineKeyboardButton(text='➡', callback_data="k3"),
        ],
    ]
)
sav3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="1"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k2"),
            InlineKeyboardButton(text='➡', callback_data="k4"),
        ],
    ]
)
sav4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="1"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k3"),
            InlineKeyboardButton(text='➡', callback_data="k5"),
        ],
    ]
)
sav5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k4"),
            InlineKeyboardButton(text='➡', callback_data="k6"),
        ],
    ]
)
sav6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="1"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k5"),
            InlineKeyboardButton(text='➡', callback_data="k7"),
        ],
    ]
)
sav7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="1"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k6"),
            InlineKeyboardButton(text='➡', callback_data="k8"),
        ],
    ]
)
sav8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="1"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k7"),
            InlineKeyboardButton(text='➡', callback_data="k9"),
        ],
    ]
)
sav9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="1"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k8"),
            InlineKeyboardButton(text='➡', callback_data="k10"),
        ],
    ]
)
sav10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="1"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k9"),
            InlineKeyboardButton(text='➡', callback_data="k11"),
        ],
    ]
)
sav11 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k10"),
            InlineKeyboardButton(text='➡', callback_data="k12"),
        ],
    ]
)
sav12 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="1"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k11"),
            InlineKeyboardButton(text='➡', callback_data="k13"),
        ],
    ]
)
sav13 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="1"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k12"),
            InlineKeyboardButton(text='➡', callback_data="k14"),
        ],
    ]
)
sav14 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="1"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k13"),
            InlineKeyboardButton(text='➡', callback_data="k15"),
        ],
    ]
)
sav15 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k14"),
            InlineKeyboardButton(text='➡', callback_data="k16"),
        ],
    ]
)
sav16 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="1"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k15"),
            InlineKeyboardButton(text='➡', callback_data="k17"),
        ],
    ]
)
sav17 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="1"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k16"),
            InlineKeyboardButton(text='➡', callback_data="k18"),
        ],
    ]
)
sav18 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="1"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="0"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k17"),
            InlineKeyboardButton(text='➡', callback_data="k19"),
        ],
    ]
)
sav19 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A", callback_data="0"),
            InlineKeyboardButton(text="B", callback_data="0"),
            InlineKeyboardButton(text="C", callback_data="1"),
            InlineKeyboardButton(text="D", callback_data="0"),
        ],
        [
            InlineKeyboardButton(text='⬅', callback_data="k18"),
            InlineKeyboardButton(text="Score", callback_data="score"),
        ],
    ]
)
