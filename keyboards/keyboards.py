from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Visual Code Studio'),
            ],
            [
                KeyboardButton(text='Sublime Text'),
            ],
            [
                KeyboardButton(text='Adobe Photoshop'),
            ],
            [
                KeyboardButton(text='Adobe Illustrator'),
            ],
            [
                KeyboardButton(text='Corel Draw'),
            ],
            [
                KeyboardButton(text='Adobe Premiere Pro'),
            ],
            [
                KeyboardButton(text='Adobe Audition'),
            ],
            [
                KeyboardButton(text='Adobe After Effects'),
            ],
    ],
            resize_keyboard=True
    )




majburiy_obuna = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Bizning kanal↗️", url="https://t.me/Xoshimjonov_Portfolio")
        ],
        [
            InlineKeyboardButton(text="Tasdiqlash",callback_data="tasdiqlash")
        ]
    ]
)