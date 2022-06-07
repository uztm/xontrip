from email import message
import logging
from unittest import skip
from aiogram import  Dispatcher, Bot , executor, types
from aiogram.types import CallbackQuery, Message
from numpy import real
import markups as nav
import dbText as tex
import cafeArena
import maps as mp
import mapru as mpru
import mapeng as mpeng
import relaxDacha as relax

from languages import lang
from markups import inkey

bot = Bot(token='5313657808:AAFKljusQ-Er5Pi0rzQQ95tQO7IklVHwR68')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)
 

# Uzbek tili

@dp.callback_query_handler(text='uz')
async def leng_uz(call: CallbackQuery):
    text = "Siz O'zbek tilini muvafoqiyatli tanladingiz!🇺🇿"
    await call.message.answer(text, reply_markup=nav.mainMenu)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.message_handler()
async def leng_u(message: Message):
    if message.text == "Tilni O'zgartirish🇺🇿":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == "Изменит Язык🇷🇺":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == "Change Language🇺🇸":
      await message.answer(f"Salom {'<b>'}{message.from_user.full_name}{'</b>'} tilni tanlang🇺🇿\n \nПривет {'<b>'}{message.from_user.full_name}{'</b>'} выбирай язык🇷🇺\n \nHello {'<b>'}{message.from_user.full_name}{'</b>'} choose a language🇺🇸",parse_mode = 'HTML', reply_markup=lang)

    if message.text == 'Xonobod 🏛':
      await message.answer("Xonobod Tarixi 🏛", reply_markup=inkey)
    
    if message.text == 'Masjidlar 🕌':
      await message.answer("Masjidlar 🕌", reply_markup=nav.MasjidlarIn)

    if message.text == 'Kafelar 🍽':
      await message.answer("Kafelar 🍽", reply_markup=cafeArena.cafeUz)

    if message.text == 'Foodbol Arenalar ⚽️':
      await message.answer("Foodbol Arenalar ⚽️", reply_markup=cafeArena.arenaUz)

    if message.text == 'Dachalar 🏕':
      await message.answer("Dachalar 🏕", reply_markup=relax.dachaUz)
    
    if message.text == 'Dam olish maskanlari 🏖':
      await message.answer("Dam olish maskanlari 🏖", reply_markup=relax.relaxUz)
    
    

    # ru
    if message.text == 'Мечети 🕌':
      await message.answer("Мечети 🕌", reply_markup=nav.MasjidlarInRu)

    if message.text == 'Кафе 🍽':
      await message.answer("Кафе 🍽", reply_markup=cafeArena.cafeRu)

    if message.text == 'Футбольные Арены ⚽️':
      await message.answer("Футбольные Арены ⚽️", reply_markup=cafeArena.arenaRu)

    if message.text == 'Дачи 🏕':
      await message.answer("Дачи 🏕", reply_markup=relax.dachaRu)

    if message.text == 'Зоны отдыха 🏖':
      await message.answer("Зоны отдыха 🏖", reply_markup=relax.relaxRu)
    
    if message.text == 'Ханобод 🏛':
      await message.answer("Ханобод 🏛", reply_markup=nav.xonobodRu)

    # eng
    if message.text == 'Mosques 🕌':
      await message.answer("Mosques 🕌", reply_markup=nav.MasjidlarInEng)
    
    if message.text == 'Cafe 🍽':
      await message.answer("Cafe 🍽", reply_markup=cafeArena.cafeEng)

    if message.text == 'Football Arenas ⚽️':
      await message.answer("Football Arenas ⚽️", reply_markup=cafeArena.arenaEng)

    if message.text == 'Dachas 🏕':
      await message.answer("Dachas 🏕", reply_markup=relax.dachaEng)

    if message.text == 'Recreation areas 🏖':
      await message.answer("Recreation areas 🏖", reply_markup=relax.relaxEng)

    if message.text == 'Khonobod 🏛':
      await message.answer("Khonobod 🏛", reply_markup=nav.XonobodEng)
# 
@dp.callback_query_handler(text="Hokim")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hokim.jpg', 'rb'), caption='HOKIMIYAT 🏛', reply_markup=mp.hokimiyat)


@dp.callback_query_handler(text="Markaz")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='Shahr Markazi 🏙', reply_markup=mp.markaz)

@dp.callback_query_handler(text="Vokzal")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Vokzal 🚉', reply_markup=mp.vogzal)

@dp.callback_query_handler(text="Bozor")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='Markaziy Dexqon Bozori 🏪', reply_markup=mp.bozor)

@dp.callback_query_handler(text="Makro")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='Makro 🏪', reply_markup=mp.makro)

@dp.callback_query_handler(text="Xontog")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Xontog ⛰', reply_markup=mp.xontog)

@dp.callback_query_handler(text="Oyingox")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Bolalar o‘yingoxi ⛹️', reply_markup=mp.oyingoh)

@dp.callback_query_handler(text="Muzey")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Abdulhay xalq amaliy sanat tarixi uy muzeyi 🏤', reply_markup=mp.muzey)



# masjid

@dp.callback_query_handler(text='Xonobod jome masjidi🕌')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption=tex.tJome, reply_markup=mp.Jome)

@dp.callback_query_handler(text='Tapalina masjidi🕌')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption=tex.tTapolino, reply_markup=mp.MasjidTop)

# choyhonalar
@dp.callback_query_handler(text='Shams choyxona 🍽')
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Shams choyxona 🍽', reply_markup=mp.ShamsMap)

@dp.callback_query_handler(text="O'tov choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='O"tov choyxona 🍽 \n\n 📞:+998999090028', reply_markup=mp.otovMap)

@dp.callback_query_handler(text="Ulfatlar choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Ulfatlar choyxona 🍽', reply_markup=mp.ulfatlarMap)

@dp.callback_query_handler(text="Afsona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Afsona 🍽', reply_markup=mp.afsonaMap)

@dp.callback_query_handler(text="Bexruz choyxonasi 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bexruz choyxonasi 🍽', reply_markup=mp.BexruzMap)

@dp.callback_query_handler(text="Majnuntol choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Majnuntol choyxona 🍽', reply_markup=mp.MajnuntolMap)

@dp.callback_query_handler(text="Oqshom Kafe 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Oqshom Kafe 🍽 \n\n 📞:+998939100907', reply_markup=mp.oqshomMap)

@dp.callback_query_handler(text="Arslon meros 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Oqshom Kafe 🍽', reply_markup=mp.arislonMap)

@dp.callback_query_handler(text="Bek oshxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bek oshxona 🍽', reply_markup=mp.bekMap)

@dp.callback_query_handler(text="Lazzat oshxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Lazzat oshxona 🍽', reply_markup=mp.lazzatMap)

@dp.callback_query_handler(text="Daxshad choyxona 🍽")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Daxshad choyxona 🍽', reply_markup=mp.daxshatMap)


# arenalar

@dp.callback_query_handler(text="Bek Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Bek Arena ⚽️', reply_markup=mp.arenaBek)

@dp.callback_query_handler(text="Dilkush Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Dilkush Arena ⚽️', reply_markup=mp.arenaDilkush)

@dp.callback_query_handler(text="Bosm Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Bosm Arena ⚽️', reply_markup=mp.arenaBosm)

@dp.callback_query_handler(text="Football Arena ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Football Arena ⚽️', reply_markup=mp.arenaFootbal)

# dachalar

@dp.callback_query_handler(text="Dacha 10 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dacha 10 🏕', reply_markup=mp.dachaOn)

@dp.callback_query_handler(text="XonDacha 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='XonDacha 🏕', reply_markup=mp.xonDacha)

@dp.callback_query_handler(text="Uy Mehmonxona 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Uy Mehmonxona 🏕', reply_markup=mp.hotelHouse)

@dp.callback_query_handler(text="Dachalar 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dachalar 🏕', reply_markup=mp.dachalar)

@dp.callback_query_handler(text="Mehmonxona 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Mehmonxona 🏕', reply_markup=mp.mehmonxona)

@dp.callback_query_handler(text="Labi Anhor 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Labi Anhor 🏕', reply_markup=mp.labiAn)

# damOlish zonalar

@dp.callback_query_handler(text="Fozilmon Ota 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Fozilmon Ota Ziyoratgoh 🏖', reply_markup=mp.fozilmon)

@dp.callback_query_handler(text="Kepmin 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Kepmin 🏖', reply_markup=mp.kepmin)

@dp.callback_query_handler(text="Oilaviy Dam Olish Maskani 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Oilaviy Dam Olish Maskani 🏖', reply_markup=mp.oilaviy)

@dp.callback_query_handler(text="Olovuddin Lager 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Olovuddin Lager 🏖', reply_markup=mp.oloviddin)

@dp.callback_query_handler(text="Andijon Soy 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Andijon Soy 🏖', reply_markup=mp.soy)


# Русский язык bot.send_photo(c.chat_id, )

@dp.callback_query_handler(text='ru')
async def leng_ru(call: CallbackQuery):
    text = "Вы успешно выбрали РУССКИЙ язык!🇷🇺"
    await call.message.answer(text, reply_markup=nav.mainMenuRu)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

# @dp.message_handler()
# async def leng_ru(message: Message):
#     if message.text == 'Xonobod 🏛':
#       await message.answer("Xonobod Tarixi 🏛", reply_markup=inkey2)


# мечеты

@dp.callback_query_handler(text='Мечеть Джоме Ханабада🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption='Мечеть Джоме Ханабада🕌', reply_markup=mpru.Jome)

@dp.callback_query_handler(text='Мечеть Топалины🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption='Мечеть Топалины🕌', reply_markup=mpru.MasjidTop)

# кафе

@dp.callback_query_handler(text='Чайхана Шамс 🍽')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Чайхана Шамс 🍽', reply_markup=mpru.ShamsMap)

@dp.callback_query_handler(text="Чайхана Отов 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='Чайхана Отов 🍽 🍽 \n\n 📞:+998999090028', reply_markup=mpru.otovMap)

@dp.callback_query_handler(text="Чайхана Ульфатлар 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Ульфатлар 🍽', reply_markup=mpru.ulfatlarMap)

@dp.callback_query_handler(text="Афсона 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Афсона 🍽', reply_markup=mpru.afsonaMap)

@dp.callback_query_handler(text="Чайхана Бехруз 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Бехруз 🍽', reply_markup=mpru.BexruzMap)

@dp.callback_query_handler(text="Чайхана Майнунтол 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Майнунтол 🍽', reply_markup=mpru.MajnuntolMap)

@dp.callback_query_handler(text="Окшом Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Окшом Кафе 🍽 \n\n 📞:+998939100907', reply_markup=mpru.oqshomMap)

@dp.callback_query_handler(text="Арслон мерос 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Арслон мерос 🍽', reply_markup=mpru.arislonMap)

@dp.callback_query_handler(text="Бек Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Бек Кафе 🍽', reply_markup=mpru.bekMap)

@dp.callback_query_handler(text="Лаззат Кафе 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Лаззат Кафе 🍽', reply_markup=mpru.lazzatMap)

@dp.callback_query_handler(text="Чайхана Дахшад 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Чайхана Дахшад 🍽', reply_markup=mpru.daxshatMap)


# football arena ru

@dp.callback_query_handler(text="Арена Бек ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Бек ⚽️', reply_markup=mpru.arenaBek)

@dp.callback_query_handler(text="Арена Дилкуш ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Дилкуш ⚽️', reply_markup=mpru.arenaDilkush)

@dp.callback_query_handler(text="Арена Босм ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Босм ⚽️', reply_markup=mpru.arenaBosm)

@dp.callback_query_handler(text="Арена Фудбол ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Арена Фудбол ⚽️', reply_markup=mpru.arenaFootbal)

# дачи

@dp.callback_query_handler(text="Дача 10 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Дача 10 🏕', reply_markup=mpru.dachaOn)

@dp.callback_query_handler(text="ХанДача 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='ХанДача 🏕', reply_markup=mpru.xonDacha)

@dp.callback_query_handler(text="Хоум Отель 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Хоум Отель 🏕', reply_markup=mpru.hotelHouse)

@dp.callback_query_handler(text="Дачи 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Дачи 🏕', reply_markup=mpru.dachalar)

@dp.callback_query_handler(text="Отель 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Отель 🏕', reply_markup=mpru.mehmonxona)

@dp.callback_query_handler(text="Лаби Анхор 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Лаби Анхор 🏕', reply_markup=mpru.labiAn)


# RELAX RU

@dp.callback_query_handler(text="Фазилмон Ота 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Фазилмон Ота 🏖', reply_markup=mpru.fozilmon)

@dp.callback_query_handler(text="Кепмин 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Кепмин 🏖', reply_markup=mpru.kepmin)

@dp.callback_query_handler(text="Семейный курорт 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Семейный курорт 🏖', reply_markup=mpru.oilaviy)

@dp.callback_query_handler(text="Оловуддин Лагер 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Оловуддин Лагер 🏖', reply_markup=mpru.oloviddin)

@dp.callback_query_handler(text="Андижан Сой 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Андижан Сой 🏖', reply_markup=mpru.soy)


# ханабад 

@dp.callback_query_handler(text="ПРАВИТЕЛЬСТВО")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hokim.jpg', 'rb'), caption='ПРАВИТЕЛЬСТВО 🏛', reply_markup=mpru.hokimiyat)


@dp.callback_query_handler(text="Центр")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='Центр города 🏙', reply_markup=mpru.markaz)

@dp.callback_query_handler(text="Вогзал")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Вогзал 🚉', reply_markup=mpru.vogzal)

@dp.callback_query_handler(text="Городской Рынок 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='Городской Рынок 🏪', reply_markup=mpru.bozor)

@dp.callback_query_handler(text="Макро 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='Макро 🏪', reply_markup=mpru.makro)

@dp.callback_query_handler(text="Хонтог ⛰")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Хонтог ⛰', reply_markup=mpru.xontog)

@dp.callback_query_handler(text="Детская площадка ⛹️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Детская площадка ⛹️', reply_markup=mpru.oyingoh)

@dp.callback_query_handler(text="музей")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Дом-музей истории народного творчества Абдулхая 🏤', reply_markup=mpru.muzey)


# English

@dp.callback_query_handler(text='eng')
async def leng_uz(call: CallbackQuery):
    text = "You have successfully chosen the ENGLISH language!🇺🇸"
    await call.message.answer(text, reply_markup=nav.mainMenuEng)
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

# musque

@dp.callback_query_handler(text='Jome Mosque Xonobod🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjid.jpg', 'rb'), caption='Jome Mosque Xonobod🕌', reply_markup=mpeng.Jome)

@dp.callback_query_handler(text='Mosque Topolina🕌')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\masjidTop.jpg', 'rb'), caption='Mosque Topolina🕌', reply_markup=mpeng.MasjidTop)

# cafe eng

@dp.callback_query_handler(text='Teahouse Shams 🍽')
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\shams.jpg', 'rb'), caption='Teahouse Shams 🍽', reply_markup=mpeng.ShamsMap)

@dp.callback_query_handler(text="Teahouse Otov 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\otov.jpg', 'rb'), caption='Teahouse Otov 🍽 \n\n 📞:+998999090028', reply_markup=mpeng.otovMap)

@dp.callback_query_handler(text="Teahouse Ulfatlar 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Ulfatlar 🍽', reply_markup=mpeng.ulfatlarMap)

@dp.callback_query_handler(text="Afsona 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Frame.jpg', 'rb'), caption='Afsona 🍽', reply_markup=mpeng.afsonaMap)

@dp.callback_query_handler(text="Teahouse Behruz 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Behruz 🍽', reply_markup=mpeng.BexruzMap)

@dp.callback_query_handler(text="Teahouse Majnuntol 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Majnuntol 🍽', reply_markup=mpeng.MajnuntolMap)

@dp.callback_query_handler(text="Okshom Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Okshom Cafe 🍽 \n\n 📞:+998939100907', reply_markup=mpeng.oqshomMap)

@dp.callback_query_handler(text="Arslon Meros 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Arslon Meros 🍽', reply_markup=mpeng.arislonMap)

@dp.callback_query_handler(text="Bek Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Bek Cafe 🍽', reply_markup=mpeng.bekMap)

@dp.callback_query_handler(text="Lazzat Cafe 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Lazzat Cafe 🍽', reply_markup=mpeng.lazzatMap)

@dp.callback_query_handler(text="Teahouse Dahshad 🍽")
async def leng_ru(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\choyxonaPlus.jpg', 'rb'), caption='Teahouse Dahshad 🍽', reply_markup=mpeng.daxshatMap)

# arenas eng

@dp.callback_query_handler(text="Arena Bek ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Bek ⚽️', reply_markup=mpeng.arenaBek)

@dp.callback_query_handler(text="Arena Dilkush ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Dilkush ⚽️', reply_markup=mpeng.arenaDilkush)

@dp.callback_query_handler(text="Arena Bosm ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Bosm ⚽️', reply_markup=mpeng.arenaBosm)

@dp.callback_query_handler(text="Arena Football ⚽️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bekaena.jpg', 'rb'), caption='Arena Football ⚽️', reply_markup=mpeng.arenaFootbal)

# dachas

@dp.callback_query_handler(text="Dacha 10")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Dacha 10 🏕', reply_markup=mpeng.dachaOn)

@dp.callback_query_handler(text="XonDacha")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xondacha.jpg', 'rb'), caption='XonDacha 🏕', reply_markup=mpeng.xonDacha)

@dp.callback_query_handler(text="Home Hotel 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Home Hotel 🏕', reply_markup=mpeng.hotelHouse)

@dp.callback_query_handler(text="Migros 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Migros 🏕', reply_markup=mpeng.dachalar)

@dp.callback_query_handler(text="Hotel 🏕")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Hotel 🏕', reply_markup=mpeng.mehmonxona)

@dp.callback_query_handler(text="Labi Anhor")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Labi.jpg', 'rb'), caption='Labi Anhor 🏕', reply_markup=mpeng.labiAn)

# relax ENG

@dp.callback_query_handler(text="Fazilmon Ota 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Fozilmon.png', 'rb'), caption='Fazilmon Ota 🏖', reply_markup=mpeng.fozilmon)

@dp.callback_query_handler(text="Kepmin")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Kempin.jpg', 'rb'), caption='Kepmin 🏖', reply_markup=mpeng.kepmin)

@dp.callback_query_handler(text="Family Resort 🏖")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Family.jpg', 'rb'), caption='Family Resort 🏖', reply_markup=mpeng.oilaviy)

@dp.callback_query_handler(text="Olovuddin Lager")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Lager.jpg', 'rb'), caption='Lager Olovuddin 🏖', reply_markup=mpeng.oloviddin)

@dp.callback_query_handler(text="Andijan Soy")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Dacha.jpg', 'rb'), caption='Andijan Soy 🏖', reply_markup=mpeng.soy)


# Khonobod

@dp.callback_query_handler(text="GOVERNMENT")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Hokim.jpg', 'rb'), caption='GOVERNMENT 🏛', reply_markup=mpeng.hokimiyat)


@dp.callback_query_handler(text="Center")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Center.JPG', 'rb'), caption='City Center 🏙', reply_markup=mpeng.markaz)

@dp.callback_query_handler(text="Railway")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Vokzal.jpg', 'rb'), caption='Railway station 🚉', reply_markup=mpeng.vogzal)

@dp.callback_query_handler(text="Market")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Bozor.jpg', 'rb'), caption='City Market 🏪', reply_markup=mpeng.bozor)

@dp.callback_query_handler(text="Makro 🏪")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Makro.jpg', 'rb'), caption='Makro 🏪', reply_markup=mpeng.makro)

@dp.callback_query_handler(text="Xontog ⛰")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Xontog.jpg', 'rb'), caption='Xontog ⛰', reply_markup=mpeng.xontog)

@dp.callback_query_handler(text="Children's playground ⛹️")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Oyingoh.jpg', 'rb'), caption='Children"s playground ⛹️', reply_markup=mpeng.oyingoh)

@dp.callback_query_handler(text="Museum")
async def leng_uz(call: CallbackQuery):
    await bot.send_photo(call.message.chat.id, open('images\Museum.jpg', 'rb'), caption='Abdulhay Folk Art History House Museum 🏤', reply_markup=mpeng.muzey)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)