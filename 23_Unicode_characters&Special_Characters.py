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

        # https://en.wikipedia.org/wiki/List_of_Unicode_characters
        self.label = Label(self.frame, text='text' + u'\u00b0', font=('Times New Roman', 32)).pack(pady=10)
        self.button = Button(self.frame, text=u'\u00BB', font=('Times New Roman', 32)).pack(pady=10)




if __name__ == '__main__':
    App()