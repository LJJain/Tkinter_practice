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

        label = Label(self.frame, text='Enter a Number')
        label.pack(pady=20)

        self.entry = Entry(self.frame)
        self.entry.pack(pady=20)

        button = Button(self.frame, text='Enter a Number', command=self.Number)
        button.pack(pady=20)

        self.label_answer = Label(self.frame, text='')
        self.label_answer.pack(pady=20)

    def Number(self):
        try:
            int(self.entry.get())
            self.label_answer.configure(text='The is Number')

        except ValueError:
            self.label_answer.configure(text='The is not Number')
        
                


if __name__ == '__main__':
    App()