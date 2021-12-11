from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sqlite_db
import time

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
            InlineKeyboardButton('Прочитать соглашение 🧐', callback_data=f'read_license')),
                           parse_mode=types.ParseMode.HTML)
    print(f'USER TO CONNECT (User_ID - {message.from_user.id}, User_Name - {message.from_user.full_name})')


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
                                      InlineKeyboardButton('Начать работу бота ⚙', callback_data=f'get_started')),
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
    global date_upd
    try:
        changes_num = float(message.text.split(' ')[1])  # Входные данные
        date_upd = f"{message.from_user.id} ({message.from_user.full_name})", int(
            time.time()), changes_num  # Выходные данные в базу данных
        await bot.send_message(chat_id=message.chat.id, text="Добавте категорию",
                               reply_markup=client_kb.inline_kb_client)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except:
        await bot.send_message(chat_id=message.chat.id, text="Введино не корректно")
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


"""
@dp.callback_query_handler(text='add_category')
Всё обработчики категорий 
"""


async def add_category(message: types.Message):
    global date_upd
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    date_upd = *date_upd, message.text
    await sqlite_db.sql_write(data_update=date_upd)
    await bot.send_message(chat_id=message.chat.id, text=f'<b>Счёт из категории</b> {message.text} успешно  добален ✅',
                           reply_markup=client_kb.kb_client, parse_mode=types.ParseMode.HTML)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Баланс Wallet 👛'))
Обработчик: Просмотр только баланса
"""


async def balance_wallet(message: types.Message):
    await sqlite_db.sql_read(message, user_id=message.from_user.id, request_type="output only balance")


"""
@dp.register_message_handler(lambda message: message.text.startswith('Посмотреть все транзакции 🔁'))
Обработчик: Просмотр всех расходов
"""


async def view_all_expenses(message: types.Message):
    await sqlite_db.sql_read(message, user_id=message.from_user.id)


"""
@dp.register_message_handler(lambda message: message.text.startswith('Посмотреть частично'))
Обработчик: Частично просмотр расходов
"""


async def view_partially_expenses(message: types.Message):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.chat.id, text='Выбери какой период:',
                           reply_markup=InlineKeyboardMarkup().row(
                               InlineKeyboardButton('3 days ☀️', callback_data=f'get_3_days'),
                               InlineKeyboardButton('5 days ☀', callback_data=f'get_5_days')).add(
                               InlineKeyboardButton('30 days ☀', callback_data=f'get_30_days')))


# Обработчик последних 3-х дней
@dp.callback_query_handler(text='get_3_days')
async def view_last_3_days(callback: types.CallbackQuery):
    await sqlite_db.sql_read(callback.message, user_id=callback.from_user.id, request_type='output 3 days')
    await callback.answer()


# Обработчик последних 5-х дней
@dp.callback_query_handler(text='get_5_days')
async def view_last_3_days(callback: types.CallbackQuery):
    await sqlite_db.sql_read(callback.message, user_id=callback.from_user.id, request_type='output 5 days')
    await callback.answer()


# Обработчик последних 30-х дней
@dp.callback_query_handler(text='get_30_days')
async def view_last_3_days(callback: types.CallbackQuery):
    await sqlite_db.sql_read(callback.message, user_id=callback.from_user.id, request_type='output 30 days')
    await callback.answer()


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
@dp.register_message_handler(lambda message: message.text.startswith('О создателе и будущих обновлений 👨‍💻'))
Обработчик: О создателе и будущих обновлений
"""


async def about_creators(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="""<b>Создатель бота: <i>Коваль Богдан</i></b>
<i>Front-End, Python  🐍  Developer  ⌨️</i>

<b>Цель бота:</b> <i>Cоздан в первую очередь для личного использование</i>

    <b>Будущее обновление ⚙:</b>
    
<i><b>В разработке и тестировании:</b>
Add option ❎: Добавлять регулярные платежи</i>

<i><b>Обновление которые вступили в силу:</b>
Debugging  ✅: Проблама чисел с плавающей тойчкой
Add option  ✅: Добавлять категории для покупок
Add option  ✅: Перевод в Unix формат времени
Add option  ✅: Просмотра расходов за последнии 3, 7, 30 дней
Upd project ✅: Оптимизирован код
Upd project ✅: Обновление безопасности
Add option  ✅: Сделать меню ещё удобней</i>

<i><b>Cooming soon:</b>
Add option ❌: Удалять/изменять пользователем счёта
Add option ❌: Полного стирание данных о пользователе
Add option ❌: Добавить достижение/ачивки
Add option ❌: Добавить аналитику росходов 
Add option ❌: Очищать историю чата
<b>And others ...</b></i>

<b>Контакты:</b>
<i>WebSite: surl.li/axmgh
GitHub: surl.li/axmtf
Email: bohdankoval3012@gmail.com</i>""", parse_mode=types.ParseMode.HTML)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


def registe_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_callback_query_handler(send_license, text='read_license')
    dp.register_callback_query_handler(get_started, text='get_started')
    dp.register_message_handler(filters_is_number,
                                lambda message: message.text.startswith('add') or message.text.startswith('Add'))
    dp.register_message_handler(add_category, lambda
        message: message.text in 'Продукты 🥦 Транспорт 🚀 Дом 🏠 Развлечения 🎡 Online Profit 🤑 Бьюти 💄 Другие ➡️')
    dp.register_message_handler(balance_wallet, lambda message: message.text.startswith('Баланс Wallet 👛'))
    dp.register_message_handler(view_all_expenses,
                                lambda message: message.text.startswith('Все транзакции 🔁'))
    dp.register_message_handler(view_partially_expenses,
                                lambda message: message.text.startswith('Частичные транзакции 🔎'))
    dp.register_message_handler(available_commands,
                                lambda message: message.text.startswith('Доступные команды 👋'))
    dp.register_message_handler(about_creators,
                                lambda message: message.text.startswith('О боте 🤖'))
