from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnMain = KeyboardButton('Bosh Sahifa')
# --- change lang ---
btnUz = KeyboardButton("Tilni O'zgartirish🇺🇿")
btnRu = KeyboardButton('Изменит Язык🇷🇺')
btnEng = KeyboardButton('Change Language🇺🇸')

# --- main menu ---
btnXonobod = KeyboardButton('Xonobod 🏛')
btnMasjid = KeyboardButton('Masjidlar 🕌')
btnKafe =  KeyboardButton('Kafelar 🍽')
btnArena = KeyboardButton('Foodbol Arenalar ⚽️')
btnChoyxona = KeyboardButton('Dam olish maskanlari 🏖')
btnDacha = KeyboardButton('Dachalar 🏕')

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobod, btnMasjid, btnKafe, btnArena, btnChoyxona, btnDacha, btnUz)

# --- manin ru ---
btnXonobodru = KeyboardButton('Ханобод 🏛')
btnMasjidru = KeyboardButton('Мечети 🕌')
btnKaferu =  KeyboardButton('Кафе 🍽')
btnArenaru = KeyboardButton('Футбольные Арены ⚽️')
btnChoyxonaru = KeyboardButton('Зоны отдыха 🏖')
btnDacharu = KeyboardButton('Дачи 🏕')

mainMenuRu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobodru, btnMasjidru, btnKaferu, btnArenaru, btnChoyxonaru, btnDacharu, btnRu)

# --- main eng ---
btnXonobodEng = KeyboardButton('Khonobod 🏛')
btnMasjidEng = KeyboardButton('Mosques 🕌')
btnKafeEng =  KeyboardButton('Cafe 🍽')
btnArenaEng = KeyboardButton('Football Arenas ⚽️')
btnChoyxonaEng = KeyboardButton('Recreation areas 🏖')
btnDachaEng = KeyboardButton('Dachas 🏕')

mainMenuEng = ReplyKeyboardMarkup(resize_keyboard= True).add(btnXonobodEng, btnMasjidEng, btnKafeEng, btnArenaEng, btnChoyxonaEng, btnDachaEng, btnEng)



# inline markups

inkey = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="HOKIMIYAT 🏛", callback_data="Hokim")
    ],
    [
      InlineKeyboardButton(text="Shahr Markazi 🏙", callback_data="Markaz"),
      InlineKeyboardButton(text="Vokzal 🚉", callback_data="Vokzal")
    ],
    [
      InlineKeyboardButton(text="Markaziy Dexqon Bozori 🏪", callback_data="Bozor")
    ],
    [
      InlineKeyboardButton(text="Makro 🏪", callback_data="Makro"),
      InlineKeyboardButton(text="Xontog' ⛰", callback_data="Xontog"),
    ],
    [
      InlineKeyboardButton(text="Bolalar o‘yingoxi ⛹️", callback_data="Oyingox")
    ],
    [
      InlineKeyboardButton(text="Abdulhay xalq amaliy sanat tarixi uy muzeyi 🏤", callback_data="Muzey")
    ],
  ]
)

xonobodRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="ПРАВИТЕЛЬСТВО 🏛", callback_data="ПРАВИТЕЛЬСТВО")
    ],
    [
      InlineKeyboardButton(text="Центр города 🏙", callback_data="Центр"),
      InlineKeyboardButton(text="Вогзал 🚉", callback_data="Вогзал")
    ],
    [
      InlineKeyboardButton(text="Городской Рынок 🏪", callback_data="Городской Рынок 🏪")
    ],
    [
      InlineKeyboardButton(text="Макро 🏪", callback_data="Макро 🏪"),
      InlineKeyboardButton(text="Хонтог ⛰", callback_data="Хонтог ⛰"),
    ],
    [
      InlineKeyboardButton(text="Детская площадка ⛹️", callback_data="Детская площадка ⛹️")
    ],
    [
      InlineKeyboardButton(text="Дом-музей истории народного творчества Абдулхая 🏤", callback_data="музей")
    ],
  ]
)

XonobodEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="GOVERNMENT 🏛", callback_data="GOVERNMENT")
    ],
    [
      InlineKeyboardButton(text="City Center 🏙", callback_data="Center"),
      InlineKeyboardButton(text="Railway station 🚉", callback_data="Railway")
    ],
    [
      InlineKeyboardButton(text="City Market 🏪", callback_data="Market")
    ],
    [
      InlineKeyboardButton(text="Makro 🏪", callback_data="Makro 🏪"),
      InlineKeyboardButton(text="Xontog' ⛰", callback_data="Xontog ⛰"),
    ],
    [
      InlineKeyboardButton(text="Children's playground ⛹️", callback_data="Children's playground ⛹️")
    ],
    [
      InlineKeyboardButton(text="Abdulhay Folk Art History House Museum 🏤", callback_data="Museum")
    ],
  ]
)






MasjidlarIn = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Xonobod jome masjidi🕌", callback_data="Xonobod jome masjidi🕌")
    ],
    [
      InlineKeyboardButton(text="Tapalina masjidi🕌", callback_data="Tapalina masjidi🕌")
    ]
  ]
)
MasjidlarInRu = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Мечеть Джоме Ханабада🕌", callback_data="Мечеть Джоме Ханабада🕌")
    ],
    [
      InlineKeyboardButton(text="Мечеть Топалины🕌", callback_data="Мечеть Топалины🕌")
    ]
  ]
)
MasjidlarInEng = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Jome Mosque Xonobod🕌", callback_data="Jome Mosque Xonobod🕌")
    ],
    [
      InlineKeyboardButton(text="Mosque Topolina🕌", callback_data="Mosque Topolina🕌")
    ]
  ]
)