import sqlite3
import time

base = sqlite3.connect('pyard.db')
cursor = base.cursor()

while True:

    sql = """
        UPDATE LED SET cond= '1' WHERE Comp='LED'
        """
    cursor.execute(sql)
    base.commit()
    time.sleep(1)
    sql = """
        UPDATE LED SET cond= '0' WHERE Comp='LED'
        """
    cursor.execute(sql)
    base.commit()
    time.sleep(1)

#DB Browser for SQLite