from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime
from keyboards import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import Wallet

"""
@dp.message_handler(commands=['start'])
"""


async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="""<b>Привет дорогой друг 👋</b>\n
Я бот кошелёк, умею хорошо считать 💭\n
Если ты хочешь знать куда ты 
потратил 15$ вчера то ты по адресу👍\n
<i>Только прочитай соглашение 📜</i>""", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Прочитать соглашение 🧐', callback_data=f'read_license')),
                           parse_mode=types.ParseMode.HTML)


"""
@dp.callback_query_handler(text='read_license')
Обработчик инлайн кнопки, просмотр лицензии
"""


async def send_license(callback: types.CallbackQuery):
    await callback.message.answer("""<b>Пользуясь @BK_Wallet_bot вы не имеете никаких притензий к @iamBohdan. И соглашаетесь с тем что он несет никаких обязанностей перед кем-либо.</b>\n
<b>Это безопасно 🔓?</b> Ничто и не когда не может гарантировать полную безопасность.\n
<b>Но все же, что я многое сделал для этого 👨‍💻.</b> Все данные в БД привязываются к вашему telegram ID.\n
<b>Всё записи храняться исключительно в зашифрованном виде 😉 . </b>И даже я не  смогу из прочитать. Так не добавлял функции для перехвата вашого запроса.\n
Давайте сделаем бота ещё круче 😎, напишите свои пожеланиие или вопросы о работе BK_Wallet. Или просто напишите спасибо 😊 (написав @iamBohdan).\n
<i>P.S. Ещё это проект Open-source, поэтому можете самы во всем убедиться</i>""",
                                  reply_markup=InlineKeyboardMarkup().add(
                                      InlineKeyboardButton(f'Начать работу бота ⚙', callback_data=f'get_started')),
                                  parse_mode=types.ParseMode.HTML)
    await callback.answer()


"""
@dp.callback_query_handler(text='get_started')
Обработчик инлайн кнопки, старт бота с возвращением клавиатуры пользователю
"""


async def get_started(callback: types.CallbackQuery):
    await callback.message.answer(text="Спасибо за доверие ☺️", reply_markup=client_kb.kb_client)
    await callback.answer()


"""
@dp.message_handler(lambda message: message.text.startswith('add'))
Основная команда для добавление изменений в Wallet
"""


async def filters_is_number(message: types.Message):
    try:
        changes_num = float(message.text.split(' ')[1])
        Wallet[datetime.now().strftime('%H:%M:%S')] = changes_num
        await bot.send_message(chat_id=message.chat.id, text=f"Число: {changes_num} добавлено")
    except:
        await bot.send_message(chat_id=message.chat.id, text="Введино не корректно")
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Посмотреть доступные команды 👋'))
Обработчик доступных функций
"""


async def available_commands(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='cooming sooon')
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('О создатели'))
Обработчик О создатели
"""


async def about_creators(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="""Front-End ⌨️, Python 🐍 Developer
Бот полностью создан @iamBohdan,
для личного ним использованием\n
Контакты:
WebSite: http://surl.li/axmgh
Git: http://surl.li/axmgk
Email: bohdankoval3012@gmail.com""")


def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(send_license, text='read_license')
    dp.register_callback_query_handler(get_started, text='get_started')
    dp.register_message_handler(filters_is_number, lambda message: message.text.startswith('add'))
    dp.register_message_handler(about_creators, lambda message: message.text.startswith('О создатели'))
    dp.register_message_handler(available_commands,
                                lambda message: message.text.startswith('Посмотреть доступные команды'))
