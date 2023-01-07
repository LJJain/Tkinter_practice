from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# 視窗 icon
# root.iconbitmap('icon file')


def open():
    global my_img
    top = Toplevel()
    top.title('My Second Window')
    my_img = ImageTk.PhotoImage(Image.open('images/book.jpg'))
    my_lab= Label(top, image=my_img).pack()
    btn2 = Button(top, text='Close Window', command=top.destroy).pack()


btn = Button(root, text='Open Second window', command=open).pack()


mainloop()