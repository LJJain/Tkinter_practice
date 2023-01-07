from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

# Drop Down Boxes
def show():
    my_lab = Label(root, text=clicked.get()).pack()

options = [
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thursday', 
    'Friday', 
    'Saturday',
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options).pack()

my_btn = Button(root, text='Show Selected', command=show).pack()

root.mainloop()