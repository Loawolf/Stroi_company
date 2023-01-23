import sqlite3 as sq

with sq.connect("Stroi.db") as con:
    cur = con.cursor()

    cur.execute("""create table Пользователи(
      login TEXT,
      password TEXT
    )
    """)
con.close()
