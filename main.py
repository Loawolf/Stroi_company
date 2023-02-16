import sqlite3 as sq
from Data_Base.Log_Reg import reg, login

with sq.connect("StroiDom.db") as con:
    cur = con.cursor()

    enter = input("Введите команду: ")
    if enter == '/reg':
        reg(input("Логин: "), input("Пароль: "))
    elif enter == '/log':
        login()
    else:
        print('Напиши команду корректно!')

con.close()
