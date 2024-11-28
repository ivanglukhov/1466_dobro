import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)
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
    CREATE TABLE IF NOT EXISTS user (
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

def get_all_adverts():
    cursor.execute('''
        SELECT * FROM advert
    ''')
    rows = cursor.fetchall()
    return rows

def get_advert(id):
    cursor.execute('''
        SELECT * FROM advert
        WHERE id='''+str(id))
    rows = cursor.fetchall()
    return rows[0]

#cursor.execute('''
#    INSERT INTO advert VALUES
#    (4, "test", "test", "test", 0, 0, "test", 0, 0)
#''')
#conn.commit()


