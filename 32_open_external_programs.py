from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

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

        self.btn = Button(self.main, text='open Program', command=self.OpenProgram)
        self.btn.pack(pady=10)

        self.btn2 = Button(self.main, text='Open Excel', command=self.OpenExcel)
        self.btn2.pack(pady=10)

        self.label = Label(self.main, text='')
        self.label.pack(pady=10)

    def OpenProgram(self):
        program = filedialog.askopenfilename()
        self.label.configure(text=program)
        # Open the program
        os.system('"%s"' % program)

    def OpenExcel(self):
        var = 'C:\Program Files\Microsoft Office\Office16\EXCEL.exe'
        os.system('"%s"' % var)

if __name__ == '__main__':
    App()