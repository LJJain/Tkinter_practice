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

        # img = Image.open('images/11.jpg')
        self.my_img = ImageTk.PhotoImage(Image.open('images/book.jpg'))
        self.my_label = Label(image=self.my_img)
        self.my_label.pack(pady=20)
        self.my_label.bind('<Enter>', self.Change)
        self.my_label.bind('<Leave>', self.ChangeBack)

    def Change(self, event):
        self.my_img = ImageTk.PhotoImage(Image.open('images/11.jpg'))
        self.my_label.config(image=self.my_img)

    def ChangeBack(self, event):
        self.my_img = ImageTk.PhotoImage(Image.open('images/book.jpg'))
        self.my_label.config(image=self.my_img)
        

if __name__ == '__main__':
    App()