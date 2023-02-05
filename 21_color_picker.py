from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')



class Main:
    def __init__(self, main):
        self.frame = Frame(main)
        self.frame.pack()

        self.button = Button(self.frame, text='Pick A Color', command=self.Color)
        self.button.pack()
    
    def Color(self):
        self.my_color = colorchooser.askcolor()[1] #取十六進制顏色編碼
        self.my_label = Label(self.frame, text=self.my_color).pack(pady=10)
        self.my_label2 = Label(self.frame, text='You Pick a Color', font=('Times New Roman', 24), bg=self.my_color).pack()

main = Main(root)
root.mainloop()