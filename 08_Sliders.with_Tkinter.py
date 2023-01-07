from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var): #把get值傳入var
    my_lab = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+'x400')

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_lab = Label(root, text=horizontal.get()).pack()


mainloop()