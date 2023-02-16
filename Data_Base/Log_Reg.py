import sqlite3
db = sqlite3.connect('StroiDom.db')
sql = db.cursor()


def login():
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")

    sql.execute(f"SELECT login FROM Пользователи WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        print("Такого пользователя не существует")

    elif sql.execute(f"SELECT login FROM Пользователи WHERE login = '{user_password}'") != sql.fetchone() is None:
        print('Вы вошли!')


def reg():
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")
    abc(user_login, user_password)


def abc(user_login, user_password):
    sql.execute(f"SELECT login FROM Пользователи WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO Пользователи VALUES (?, ?)",
                    (user_login, user_password))
        db.commit()
        print('Вы успешно зарегистрировались!')
    else:
        print('Такой пользователь уже существует!')
