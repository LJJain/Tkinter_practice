from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

options = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]
clicked = StringVar()
clicked.set(options[0])

class name:
    def __init__(self, main):
        self.frame = Frame(main)
        self.frame.pack()

        self.drop = OptionMenu(main, clicked, *options, command=self.select)
        self.drop.pack(pady=20)

        self.combo = ttk.Combobox(self.frame, value=options)
        self.combo.current(0)
        self.combo.bind('<<ComboboxSelected>>', self.comboclick)
        self.combo.pack()

        # self.dtn = Button(main,text='Select from list', command=self.select)
        # self.dtn.pack()

    def select(self, event):
        # lab_1 = Label(self.frame, text=clicked.get()).pack()
        if clicked.get() == 'Friday':
            lab_1 = Label(self.frame, text="Ya! It's Friday").pack()
        else:
            lab_1 = Label(self.frame, text=clicked.get()).pack()

    def comboclick(self, event):
        lab_1 = Label(self.frame, text=self.combo.get()).pack()

e = name(root)
root.mainloop()