from tkinter import *
from PIL import ImageTk, Image

def App():
    root = Tk()
    root.title('Learn To Code Tkinter')
    # root.iconbitmap('icon file')
    root.geometry('800x600')

    app = Main(root)
    root.mainloop()

class Main():
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        w = 600
        h = 400
        x = w//2
        y = h//2

        self.canvas = Canvas(self.main, width=w, height=h, bg='white')
        self.canvas.pack()

        self.circle =self.canvas.create_oval(x, y, x+10, y+10)

        self.main.bind('<Left>', self.Left)
        self.main.bind('<Right>', self.Right)
        self.main.bind('<Up>', self.Up)
        self.main.bind('<Down>', self.Down)

    def Left(self, event):
        x = -10
        y = 0
        self.canvas.move(self.circle, x, y)

    def Right(self, event):
        x = 10
        y = 0
        self.canvas.move(self.circle, x, y)

    def Up(self, event):
        x = 0
        y = -10
        self.canvas.move(self.circle, x, y)

    def Down(self, event):
        x = 0
        y = 10
        self.canvas.move(self.circle, x, y)

        

if __name__ == '__main__':
    App()