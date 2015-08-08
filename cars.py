import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute(
    """CREATE TABLE inventory
    (Make TEXT, Model TEXT, Quantity TEXT)""")

conn.close()