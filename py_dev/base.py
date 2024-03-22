import asyncio
import datetime
from time import sleep

import asyncpg

from configs import Settings


INSERT_INTO = ('INSERT INTO users(name, dob) VALUES($1, $2)')


async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect(
        database=Settings.POSTGRES_NAME,
        user=Settings.POSTGRES_USER,
        password=Settings.POSTGRES_PASSWORD,
        host=Settings.DB_HOST,
        port=Settings.DB_PORT
    )
    # # Execute a statement to create a new table.
    print('Успешно добавленна таблица')
    # sleep(2)
    # await conn.execute(DELETE_TABLE)
    # print('Успешно удаленна таблица')

    # # Insert a record into the created table.
    # await conn.execute(INSERT_INTO, 'Bob', datetime.date(1984, 3, 1))

    # # Select a row from the table.
    # row = await conn.fetchrow('SELECT * FROM users WHERE name = $1', 'Bob')
    # # *row* now contains
    # # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))
    # print(row)

    await conn.close()

asyncio.get_event_loop().run_until_complete(main())
