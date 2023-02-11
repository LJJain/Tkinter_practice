from tkinter import *
from PIL import ImageTk, Image

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

        self.label = Label(self.frame, text='This is a text', font=('Times New Roman', 20))
        self.label.pack(pady=10)

        self.button = Button(self.frame, text='This is a button', command=self.Something)
        self.button.pack(pady=10)

    def Something(self):
        self.label.config(text='This is new text !!')
        self.main.config(bg='blue')
        self.button.config(text="You've been configged !!", state=DISABLED)





if __name__ == '__main__':
    App()