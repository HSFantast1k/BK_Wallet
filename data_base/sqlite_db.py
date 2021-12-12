import sqlite3 as sq
import time
from create_bot import bot
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

"""
Создание базы данных
"""


def sql_start():
    global base, cur
    base = sq.connect('main_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute("""CREATE TABLE IF NOT EXISTS oper(
    Tg_ID TEXT,
    Date INT PRIMARY KEY,
    Operations INT,
    Category TEXT);
    """)
    base.commit()


"""
Запись в базу данных
"""


async def sql_write(data_update):
    # print(f"data update {data_update}")
    cur.execute("INSERT INTO oper VALUES (?,?,?,?)", data_update)
    base.commit()


"""
Полное\Частичное чтение из БД

Функция sql_read принимаеть второй аргумен request_type - тип операции (по умолчанию он равен output everything - вывод всё),
можна изменить на output only balance - вывод только баланса, output 3 days - вывод посденних 3 дней

"""


async def sql_read(message, user_id, request_type="output everything"):
    total_spent = 0
    for cell in cur.execute('SELECT * FROM oper').fetchall():
        if int(str(cell[0]).split(' ')[0]) == user_id:
            if 'days' not in request_type:
                if request_type == "output everything":
                    await bot.send_message(chat_id=message.chat.id,
                                           text=f'<b>Дата операции:</b> {datetime.fromtimestamp(cell[1])}\n<b>Сума:</b> {cell[2]} UAH\n<b>Категория:</b> {cell[3]}',
                                           parse_mode=types.ParseMode.HTML,
                                           reply_markup=InlineKeyboardMarkup().add(
                                               InlineKeyboardButton(f'Удалить ❌',
                                                                    callback_data=f'del {cell[1]}')))
                total_spent += round(cell[2], 2)
            elif 'days' in request_type and (
                    int(time.time()) - cell[1]) <= int(request_type.split(' ')[1]) * 24 * 60 * 60:
                await bot.send_message(chat_id=message.chat.id,
                                       text=f'<b>Дата операции:</b> {datetime.fromtimestamp(cell[1])}\n<b>Сума:</b> {cell[2]} UAH\n<b>Категория:</b> {cell[3]}',
                                       parse_mode=types.ParseMode.HTML)
                total_spent += round(cell[2], 2)
    await bot.send_message(chat_id=message.chat.id, text=f"<b>Последний баланс Wallet:</b> {round(total_spent, 2)} UAH",
                           parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id=message.chat.id, text='―' * 10)


"""
Выборочное удаление операций из БД, через Inline btn
"""


async def sql_delete_cell(date):
    cur.execute('DELETE FROM oper WHERE Date == ?', (date,))
    base.commit()
