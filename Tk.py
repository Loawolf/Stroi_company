from tkinter import *
from PIL import Image, ImageTk

root = Tk()


class main_menu():
    def start():
        bluesky = Label(
            text='Добро пожаловать!')
        bluesky.pack()
        root.mainloop()

    def pic():
        canvas = Canvas(root)
        image = Image.open(
            "pics\Bluesky-announced-new-decentralized-social-network.png")
        photo = ImageTk.PhotoImage(image)
        image = canvas.create_image(0, 0, anchor='nw', image=photo)
        canvas.grid(row=2, column=1)
        root.mainloop()


main_menu.start()
