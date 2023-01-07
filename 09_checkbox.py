from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')

var = IntVar()
c = Checkbutton(root, text='check this box', variable=var).pack()

myLabel = Label = Label(root, text=var.get()).pack()


mainloop()