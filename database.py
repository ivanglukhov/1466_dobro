import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS advert (
         id INTEGER PRIMARY KEY,
         adress VARCHAR,
         header VARCHAR,
         description TEXT,
         service_mode INTEGER,
         creator INTEGER,
         image VARCHAR,
         volunt_number INTEGER,
         respond INTEGER
    )
''')

conn.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS advert (
         id INTEGER PRIMARY KEY,
         role VARCHAR,
         adress VARCHAR,
         name VARCHAR,
         rating REAL,
         age INTEGER,
         phone VARCHAR
    )
''')

conn.commit()