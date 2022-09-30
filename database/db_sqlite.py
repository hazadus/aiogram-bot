import os
import logging

import sqlite3 as sql


def sqlite_start():
    global db, cursor
    db = sql.connect(os.getenv('BOT_SQLITE_FILENAME'))
    cursor = db.cursor()

    if db:
        logging.info(f"Connected to SQLite DB {os.getenv('BOT_SQLITE_FILENAME')}")
        db.execute("CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)")
        db.commit()
    else:
        logging.error(f"Connection to SQLite DB {os.getenv('BOT_SQLITE_FILENAME')} failed!")


async def sqlite_add_product(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        db.commit()


def sqlite_get_all_products():
    return cursor.execute('SELECT * FROM menu').fetchall()
