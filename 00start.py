# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# root.title('Learn To Code Tkinter')
# # root.iconbitmap('icon file')
# root.geometry('400x400')

# root.mainloop()

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# 視窗 icon
# root.iconbitmap('icon file')

my_img = ImageTk.PhotoImage(Image.open('images/rose_coffee.png'))
my_label = Label(image=my_img)
my_label.pack()


e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    hello = 'Hello ' + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click Me", padx=10, pady=10, command=myClick, fg="blue", bg='red')
myButton.pack()

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()

my_img1 = ImageTk.PhotoImage(Image.open('images/11.jpg'))
my_label = Button(root, text='text' ,image=my_img1, compound = TOP).pack()


root.mainloop()

# Classify Method

# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# root.title('Learn To Code Tkinter')
# # root.iconbitmap('icon file')
# root.geometry('400x400')


# class name:
#     def __init__(self, main):
#         self.frame = Frame(main)
#         self.frame.pack()

# e = name(root)
# root.mainloop()