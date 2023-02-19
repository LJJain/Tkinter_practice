from tkinter import *
from PIL import ImageTk, Image
from tkcalendar import *

def App():
    root = Tk()
    root.title('Learn To Code Tkinter')
    # root.iconbitmap('icon file')
    root.geometry('400x400')

    app = Main(root)
    root.mainloop()

class Main():
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.cal = Calendar(self.main, selectmode='day', year=2022, month=5, day=8)
        self.cal.pack(pady=20, fill=BOTH, expand=True)

        btn = Button(self.main, text='Get Date', command=self.GrabDate)
        btn.pack(pady=20)

        self.label = Label(self.main, text='')
        self.label.pack(pady=20)

    def GrabDate(self):
        self.label.config(text=self.cal.get_date())

        
if __name__ == '__main__':
    App()