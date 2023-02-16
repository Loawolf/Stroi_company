from tkinter import *
from PIL import Image, ImageTk
from Data_Base.Log_Reg import reg, login

root = Tk()


class main_menu():

    def pic(a):
        canvas = Canvas(root)
        image = Image.open(
            a)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.grid(row=2, column=1)

    def start():

        Label(
            text='Добро пожаловать!\n Для дальнейшей работы войдите или зарегистрируйтесь.').grid(row=1, column=1)
        v = Button(text='Войти', command=main_menu.entr)
        v.grid(row=2, column=0)
        l = Button(text='Зарегистрироваться', command=main_menu.log)
        l.grid(row=2, column=1)
       # main_menu.pic('pics\Bluesky-announced-new-decentralized-social-network.png')

    def entr():
        entr = Toplevel()
        Label(entr, text='Авторизация').grid(columnspan=2)
        Label(entr, text='Логин').grid(row=1, column=0)
        Label(entr, text='Пароль').grid(row=2, column=0)
        l = Entry(entr)
        l.grid(row=1, column=1)
        p = Entry(entr, show='*')
        p.grid(row=2, column=1)
        Button(entr, text='Войти', command=main_menu.pol(
            l, p)).grid(row=3, column=1)

    def pol(l, p):
        l, p = l.get, p.get
        reg(l, p)

    def log():
        lo = Toplevel()
        Label(lo, text='Регистрация').grid(columnspan=2)
        Label(lo, text='Логин').grid(row=1, column=0)
        Label(lo, text='Пароль').grid(row=2, column=0)
        l = Entry(lo)
        l.grid(row=1, column=1)
        p = Entry(lo, show='*')
        p.grid(row=2, column=1)
        Button(lo, text='Войти', command=login(
            l.get, p.get)).grid(row=3, column=1)


main_menu.start()
root.mainloop()
