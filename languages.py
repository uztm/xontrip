from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="UZ🇺🇿", callback_data="uz"),
      InlineKeyboardButton(text="RU🇷🇺", callback_data="ru"),
      InlineKeyboardButton(text="ENG🇺🇸", callback_data="eng"),
    ]
  ]
)