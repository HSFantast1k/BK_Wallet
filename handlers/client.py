from aiogram import types, Dispatcher
from create_bot import dp, bot
from datetime import datetime
from keyboards import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sqlite_db

from create_bot import Wallet

"""
@dp.message_handler(commands=['start'])
"""


async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="""<b><i>Привет дорогой друг 👋</i></b>\n
Я бот кошелёк, умею хорошо считать 💭\n
Если ты хочешь знать куда ты 
потратил 15$ вчера, то ты по адресу👍\n
<i>Только прочитай соглашение 📜</i>""", reply_markup=InlineKeyboardMarkup().add(
            InlineKeyboardButton(f'Прочитать соглашение 🧐', callback_data=f'read_license')),
                           parse_mode=types.ParseMode.HTML)


"""
@dp.callback_query_handler(text='read_license')
Обработчик инлайн кнопки, просмотр лицензии
"""


async def send_license(callback: types.CallbackQuery):
    await callback.message.answer("""<b>Пользуясь @BK_Wallet_bot вы не имеете никаких притензий к @iamBohdan. 
И соглашаетесь с тем что он несет никаких обязанностей перед кем-либо.</b>

<b>Это безопасно 🔓?</b> Ничто и не когда не может гарантировать полную безопасность.

<b>Но все же, я многое сделал для этого 👨‍💻.</b> Все данные в БД привязываются к вашему telegram ID.

<b>Всё записи храняться исключительно в зашифрованном виде 😉 . </b>И даже я не  смогу из прочитать. Так не добавлял функции для перехвата вашого запроса.

<b>Давайте сделаем бота ещё круче 😎,</b> напишите свои пожеланиие или вопросы о работе BK_Wallet 🗳. Или просто напишите спасибо 😊 (написав @iamBohdan).


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
        Wallet[datetime.now().strftime('%Y-%m-%d %H:%M:%S')] = changes_num
        date_upd = f"{message.from_user.id} ({message.from_user.full_name})", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), changes_num
        print(f"Telegram ID: {message.from_user.id}, Suma: {sum(Wallet.values())}, Wallet: {Wallet}")

        await bot.send_message(chat_id=message.chat.id, text=f"База данных обновлена")
        await sqlite_db.sql_write(data_update=date_upd)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except:
        await bot.send_message(chat_id=message.chat.id, text="Введино не корректно")
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Посмотреть доступные команды 👋'))
Обработчик: Доступных функций
"""


async def available_commands(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="""<b>Доступные комманды:</b>
    
<b>add N - основная команда для изменение счёта,</b> 
где N положительное или отрицательное - число на которые хотите добавить или списать счёт соотвественно. 
<b>Например:</b> add -5, означает что вы потратели 5$, add 5 что вы заработали 5$""",
                           parse_mode=types.ParseMode.HTML)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Посмотреть все расходы 💰'))
Обработчик: Просмотр всех расходов
"""


async def view_all_expenses(message: types.Message):
    await sqlite_db.sql_read(message)
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Баланс Wallet 👛'))
Обработчик: Просмотр только баланса
"""


async def balance_wallet(message: types.Message):
    await sqlite_db.sql_read(message, request_type="output only balance")
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('О создатели'))
Обработчик: О создателе и будущих обновлений
"""


async def about_creators(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="""<b>Создатель бота: <i>Коваль Богдан</i></b>
<i>Front-End, Python  🐍  Developer  ⌨️</i>

<b>Цель бота:</b> <i>Cоздан в первую очередь для личного использование</i>

    <b>Будущее обновление ⚙:</b>
    
<b><i>В разработке и тестировании:</i></b>
<i>Add option ❎: Добавлять категории для покупок</i>

<b><i>Обновление вступили в силу:</i></b>
<i>Debugging ✅: Проблама чисел с плавающей тойчкой</i>

<b><i>Cooming soon:</i></b>
<i>Add option ❌: Очищать историю чата
Add option ❌: Просмотра расходов за последнии 3, 7, 30 дней
Add option ❌: Сделать меню ещё удобней
Add option ❌: Добавлять подписки
Add option ❌: Удалять/изменять пользователем счёта
Add option ❌: Полного стирание данных о пользователе
</i>
<b>Контакты:</b>
<i>WebSite: surl.li/axmgh</i>
<i>GitHub: surl.li/axmtf</i>
<i>Email: bohdankoval3012@gmail.com</i>""", parse_mode=types.ParseMode.HTML)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(send_license, text='read_license')
    dp.register_callback_query_handler(get_started, text='get_started')
    dp.register_message_handler(filters_is_number, lambda message: message.text.startswith('add'))
    dp.register_message_handler(available_commands,
                                lambda message: message.text.startswith('Посмотреть доступные команды 👋'))
    dp.register_message_handler(view_all_expenses, lambda message: message.text.startswith('Посмотреть все расходы 💰'))
    dp.register_message_handler(balance_wallet, lambda message: message.text.startswith('Баланс Wallet 👛'))
    dp.register_message_handler(about_creators, lambda message: message.text.startswith('О создателе и будущих обновлений 👨‍💻'))
