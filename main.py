import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from config import BOT_TOKEN
from aiogram.filters import Command
from bs4.builder import HTML
import keyboards as kb
from api import hamma_vaqtlar
logging.basicConfig(level=logging.INFO)

from aiohttp import web

# 1. Koyeb uxlab qolmasligi uchun kichik veb-server
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_fake_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Koyeb taqdim etadigan PORT orqali ishga tushadi
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# 2. Botni ishga tushirish funksiyasi
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Parallel ravishda veb-serverni ham ishga tushiramiz
    asyncio.create_task(start_fake_server())

    print("Bot muvaffaqiyatli ishga tushdi...")
    # Bu yerda sizning barcha handlerlaringiz (start, menu va h.k.) bo'lishi kerak
    # Masalan: dp.include_router(your_router)
    
    await dp.start_polling(bot)

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
#start komandasi berilgandagi buyruqlar--------------------------------
@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(f"Assalomu Aleykum <b>{user_name}</b> ! Bu botga xush kelibsiz.", reply_markup=kb.main_menu,parse_mode=HTML)

#--BOT haqida--------------------------------------------------------------------------------
@dp.message(F.text == "Bot Haqida")
async def bot_info(message: types.Message):
        text = (
        f"Mazkur bot foydalanuvchilarga namoz vaqtlari va diniy ma'lumotlarni qulay tarzda yetkazish maqsadida ishlab chiqildi.\n"
        f"⚠️<b>Muhim eslatma</b>: Botimiz noto'g'ri yoki asossiz ma'lumotlar tarqatishdan mutlaqo yiroq. Barcha taqvimlar,"
        f" namoz vaqtlari va diniy manbalar O‘zbekiston Musulmonlari idorasi (muslim.uz) hamda islom.uz portali kabi "
        f"rasmiy va ishonchli manbalardan olingan.\n" 

        f"🎯<b>Maqsadimiz</b>: Sizga ibodatlaringizda ko'makchi bo'lish va faqatgina tasdiqlangan, shar'iy jihatdan to'g'ri ma'lumotlarni taqdim etishdir\n."

        f"<i><b>Alloh ibodatlaringizni qabul qilsin!</b></i>\n"
        f"Asosiy manbalar https://namozvaqti.uz/ va https://islom.uz/ "
        )
        await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)
#Ilm maskani uchun--------------------------------------------------------------------------
@dp.message(F.text == "Ilm maskani")
async def ilm_maskani(message: types.Message):
    await message.answer(
        "Ilm maskaniga hush kelibsiz:",
        reply_markup=kb.ilm_maskani
    )

#--Ramazon Taqvimi---------------------------------------------------------------------------

@dp.message(F.text == "Taqvim")
async def ramazon_vaqtlari(message: types.Message):
    await message.answer(
        "Taqvimni bilishi uchun shaharni tanlang:",
        reply_markup=kb.namoz_times
    )
#-baza--------------------------------------------------------------------------------------------
viloyatlar_lugati = {
    "toshkent": kb.toshkent_tuman,
    "namangan": kb.namangan_tuman,
    "andijon": kb.andijon_tuman,
    "fargona": kb.fargona_tuman,
    "jizzax": kb.jizzax_tuman,
    "surxandaryo": kb.surxandaryo_tuman,
    "buxoro": kb.buxoro_tuman,
    "navoiy": kb.navoiy_tuman,
    "qashqadaro": kb.qashqadaryo_tuman,
    "samarqand": kb.samarqand_tuman,
    "qoraqalpogiston": kb.qoraqalpogiston_tuman,
    "xorazm": kb.xorazm_tuman,
    "sirdaryo": kb.sirdaryo_tuman
}
taqvim_rasmlari = {
    "toshkent": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "namangan": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "andijon": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "fargona": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "jizzax": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "surxandaryo": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "buxoro": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "navoiy": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "qashqadaro": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "samarqand": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "qoraqalpogiston": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "xorazm": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ',
    "sirdaryo": 'AgACAgIAAxkBAAOMaUrfSWnlBbfBybgl7T3BdYIAAdkCAALuDWsb_y9ASaZW0wd6Y8xmAQADAgADeQADNgQ'
}


@dp.callback_query()
async def universal_callback_handler(callback: types.CallbackQuery):
    data = callback.data

#orqaga qaytish tugmasi ----------------------------------------------
    if data == "back_to_main":
        await callback.message.edit_text(
            "Viloyatni tanlang:",
            reply_markup=kb.namoz_times
        )
        await callback.answer()
        return

#oylik taqvim --------------------------------------------------------
    elif data.startswith("full_taqvim:"):
        shahar_nomi = data.split(":")[1]
        file_id = taqvim_rasmlari.get(shahar_nomi)

        if not file_id:
            #Viloyat shaharlarini ajrati bolish
            for viloyat, keyboard in viloyatlar_lugati.items():
                if any(shahar_nomi in str(btn) for row in keyboard.inline_keyboard for btn in row):
                    file_id = taqvim_rasmlari.get(viloyat.replace("_uz", ""))
                    break
        if file_id:
            await callback.message.answer_photo(
                photo=file_id,
                caption=f"🌙 <b>{shahar_nomi.capitalize()}</b> uchun butun oylik taqvim.",
                parse_mode="HTML"
            )
        else:
            await callback.answer("Bu hudud uchun rasm topilmadi!", show_alert=True)
        await callback.answer()
        return

#tumanni tanlash-------------------------------------------------------
    elif data in viloyatlar_lugati:
        await callback.message.edit_text(
            "Tumanni tanlang:",
            reply_markup=viloyatlar_lugati[data]
        )
        await callback.answer()
        return
#viloyat markazlari uchun taqvim---------------------------------------
    elif data.endswith("_uz"):
        shahar = data.replace("_uz", "")  # '_uz' ni olib tashlaymiz: 'toshkent_uz' -> 'toshkent'
        v = await hamma_vaqtlar(shahar)
        if v:
            text = (
                f"📍 <b>{shahar.capitalize()}: {v['shahar']}</b>\n\n"
                f"🏙 <b>Saharlik: {v['bomdod']} gacha</b>\n"
                f"🌆 <b>Iftorlik: {v['shom']} dan so'ng</b>\n\n"
                f"<i><b>Namoz vaqtlari</b></i>\n"
                f"🏙 <b>Bamdod: {v['bomdod']}</b>\n"
                f"🌅 <b>Quyosh: {v['quyosh']}</b>\n"
                f"☀️ <b>Peshin: {v['peshin']}</b>\n"
                f"🏞 <b>Asr: {v['asr']}</b>\n"
                f"🌆 <b>Shom: {v['shom']}</b>\n"
                f"🌃 <b>Xufton: {v['xufton']}</b>\n\n"
                f"<i>Manba: namozvaqti.uz</i>"
            )

            await callback.message.edit_text(
                text,
                reply_markup=kb.get_tuman_markup(shahar),
                parse_mode='html'
            )
        await callback.answer()
        return
#tuman va viloyatlar uchun vaqtlar --------------------------------------
    else:
        try:

            v = await hamma_vaqtlar(data)

            if v:
                text = (
                    f"📍 <b>{data.capitalize()}: {v['shahar']}</b>\n\n"
                    f"🏙 <b>Saharlik: {v['bomdod']} gacha</b>\n"
                    f"🌆 <b>Iftorlik: {v['shom']} dan so'ng</b>\n\n"
                     f"<i><b>Namoz vaqtlari</b></i>\n"
                    f"🏙 <b>Bamdod: {v['bomdod']}</b>\n"
                    f"🌅 <b>Quyosh: {v['quyosh']}</b>\n"
                    f"☀️ <b>Peshin: {v['peshin']}</b>\n"
                    f"🏞 <b>Asr: {v['asr']}</b>\n"
                    f"🌆 <b>Shom: {v['shom']}</b>\n"
                    f"🌃 <b>Xufton: {v['xufton']}</b>\n\n"
                    f"<i>Manba: namozvaqti.uz</i>"
                )

                markup = kb.get_tuman_markup(data)
                await callback.message.edit_text(
                    text=text,
                    reply_markup=markup,
                    parse_mode='HTML'
                )
            else:
                await callback.answer("Ma'lumot topilmadi.", show_alert=True)
                await callback.answer()
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            await callback.answer("Texnik xatolik yuz berdi.")
#------------------------------------

@dp.message(F.photo)
async def get_ids_from_channel(message: types.Message):
    photo_id = message.photo[-1].file_id
    caption = message.caption or "noma'lum"
    print(f'"{caption.lower()}": "{photo_id}",')
    await message.answer(f"✅ {caption} uchun ID olindi va terminalga chiqarildi.")
#--BOT ishga tushirish qism-----------------------------------------------------------------
async def main():
    
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot o'chirildi.")
    except Exception as e:

        print(f"Kutilmagan xato: {e}")


