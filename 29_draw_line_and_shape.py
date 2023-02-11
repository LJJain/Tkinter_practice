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

        self.canvas = Canvas(self.frame, width=300, height=300, bg='white')
        self.canvas.pack(pady=20)

        # Create Line
        # self.canvas.create_line(x1, y1, x2, y2, fill='color')
        self.canvas.create_line(0, 100, 300, 100, fill='red')

        # Create Rectangle
        # self.canvas.create_rectangle(x1, y1, x2, y2, fill='color')
        # x1, y1 = Top Left ; x2, y2 = Bottom Right
        self.canvas.create_rectangle(50, 150, 250, 50, fill='pink')

        # Create Oval
        # self.canvas.create_oval(50, 150, 250, 50, fill='cyan')
        # x1, y1 = Top Left ; x2, y2 = Bottom Right
        self.canvas.create_oval(50, 150, 250, 50, fill='cyan')



if __name__ == '__main__':
    App()