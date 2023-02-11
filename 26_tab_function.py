from tkinter import *
from tkinter import ttk
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

        self.notebook = ttk.Notebook(self.frame)
        self.notebook.pack(pady=15)

        self.frame_1 = Frame(self.notebook, width=500, height=500, bg='blue')
        self.frame_2 = Frame(self.notebook, width=500, height=500, bg='red')
        self.frame_1.pack(fill=BOTH, expand=1)
        self.frame_2.pack(fill=BOTH, expand=1)

        self.notebook.add(self.frame_1, text='Blue Tab')
        self.notebook.add(self.frame_2, text='Red Tab')

        self.button_hide = Button(self.frame_1, text='Hide Tab 2', command=self.Hide)
        self.button_hide.pack(pady=10)

        self.button_show = Button(self.frame_1, text='Show Tab 2', command=self.Show)
        self.button_show.pack(pady=10)

        # Navigate to a tab
        self.button_navigate = Button(self.frame_1, text='Navigate Tab', command=self.Select)
        self.button_navigate.pack(pady=10)

    def Hide(self):
        self.notebook.hide(1)

    def Show(self):
        self.notebook.add(self.frame_2, text='Red Tab')

    def Select(self):
        self.notebook.select(1)





if __name__ == '__main__':
    App()