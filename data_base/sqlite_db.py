import sqlite3 as sq
from create_bot import bot
from aiogram import types

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
    Date TEXT,
    Operations INT);
    """)
    base.commit()


"""
Запись в базу данных
"""


async def sql_write(data_update):
    print(f"data update {data_update}")
    cur.execute("INSERT INTO oper VALUES (?,?,?)", data_update)
    base.commit()


"""
Полное чтение из БД

Функция sql_read принимаеть второй аргумен request_type - тип операции (по умолчанию он равен output everything - вывод всё),
можна изменить на output only balance - вывод только баланса
"""


async def sql_read(message, request_type="output everything"):
    total_spent = 0
    for cell in cur.execute('SELECT * FROM oper').fetchall():
        if int(str(cell[0]).split(' ')[0]) == message.from_user.id:
            if request_type == "output everything":
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f'<b>Дата операции:</b> {cell[1]}\n<b>Сума:</b> {cell[2]}',
                                       parse_mode=types.ParseMode.HTML)
            total_spent += cell[2]
    await bot.send_message(chat_id=message.from_user.id, text=f"<b>Баланс Wallet:</b> {total_spent} $",
                           parse_mode=types.ParseMode.HTML)
    await bot.send_message(chat_id=message.from_user.id, text='-' * 10)
