from tkinter import *
from PIL import Image, ImageTk

root = Tk()


class main_menu():

    def pic(a):
        canvas = Canvas(root)
        image = Image.open(
            a)
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.grid(row=2, column=1)
        root.mainloop()

    def start():
        bluesky = Label(
            text='Добро пожаловать!')
        bluesky.grid(row=1, column=1)
        b = Button(text='Закрыть все', command=main_menu.close)
        b.grid(row=2, column=1)
       # main_menu.pic('pics\Bluesky-announced-new-decentralized-social-network.png')
        root.mainloop()

    def close(*any):

        root.destroy()


main_menu.start()
