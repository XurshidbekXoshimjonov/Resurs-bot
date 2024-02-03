from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu3 = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Dasturlash'),
                KeyboardButton(text="Grafik dizayn"),
            ],
            [
                KeyboardButton(text="Video montaj"),
                KeyboardButton(text="Axborot va Media")
            ],
            [
                KeyboardButton(text="Boshqa dasturlar"),
                KeyboardButton(text="🔝 Asosiy menu")
            ]
                
    ],
    resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Visual Code Studio'),
                KeyboardButton(text='Sublime Text'),
            ],
            [
                KeyboardButton(text='PyCharm'),
                KeyboardButton(text='🔙 Orqaga')
            ],
    ],
            resize_keyboard=True
    )

grafik_dizayn = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Adobe Photoshop'),
                KeyboardButton(text='Adobe Illustrator')
            ],
            [
                KeyboardButton(text='Corel Draw'),
                KeyboardButton(text='Adobe Photoshop Lightroom')
            ],
            [
                KeyboardButton(text='🔙 Orqaga')
            ]
    ],
            resize_keyboard=True
    )

video_montaj = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Adobe Premiere Pro'),
                KeyboardButton(text='Adobe Audition')
            ],
            [
                KeyboardButton(text='Adobe After Effects'),
                KeyboardButton(text='VFX Suite')
            ],
            [
                KeyboardButton(text='Universe'),
                KeyboardButton(text='TrapCode Suite')
            ],
            [
                KeyboardButton(text='DaVinci'),
                KeyboardButton(text='Screen Recorder')
            ],
            [
                KeyboardButton(text='🔙 Orqaga')
            ]
    ],
            resize_keyboard=True
    )


table = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Dasturlar'),
                KeyboardButton(text="O'rnatish videolari"),
            ],
            [
                KeyboardButton(text="Bot haqida"),
                KeyboardButton(text="Darslarimiz")
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




menu2 = ReplyKeyboardMarkup(
    keyboard=[
              [
                KeyboardButton(text="VS Code o'rnatish videosi"),
                KeyboardButton(text="Sublime Text o'rnatish videosi ")
            ],
            [
                KeyboardButton(text="Adobe Photoshop o'rnatish videosi "),
                KeyboardButton(text="Adobe Illustrator o'rnatish videosi "),
                KeyboardButton(text="Corel Draw o'rnatish videosi ")
            ],
            [
                KeyboardButton(text="Adobe Premiere Pro o'rnatish videosi "),
                KeyboardButton(text="Adobe Audition o'rnatish videosi "),
                KeyboardButton(text="Adobe After Effects o'rnatish videosi ")
            ],
            [
                KeyboardButton(text='🔝 Asosiy menu'),
            ],
    ],
            resize_keyboard=True
    )




media = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Adobe Animate'),
                KeyboardButton(text="Adobe Media Encover"),
            ],
            [
                KeyboardButton(text="🔙 Orqaga"),
            ],
                
    ],
    resize_keyboard=True
)


dasturlar = ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(text='Adobe InDesign'),
                KeyboardButton(text="Adobe InCopy"),
            ],
            [
                KeyboardButton(text="🔙 Orqaga"),
            ],
                
    ],
    resize_keyboard=True
)