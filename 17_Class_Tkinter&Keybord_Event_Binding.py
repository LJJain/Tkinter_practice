from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

class name:
    def __init__(self, main):
        self.frame = Frame(main)
        self.frame.pack()

        # self.btn_1 = Button(self.frame, text='Click Me!', command=self.clicker)
        self.btn_1 = Button(self.frame, text='Click Me!')   # Keyboard Event Binding
        self.btn_1.bind('<Key>', self.clicker) # Button-1:滑鼠左鍵, Button-2:滑鼠中鍵, Button-3:滑鼠右鍵, Enter:滑鼠進入, Leave:滑鼠離開, Return:鍵盤Enter
        self.btn_1.pack(pady=20)

    def clicker(self, event):
        # lab_1 = Label(self.frame, text='You clicked a button!' + str(event.x) + " " + str(event.y)).pack()
        lab_1 = Label(self.frame, text='You clicked a button!' + event.keysym).pack() # keysym: 按鍵名稱
        # print('Look at you...you clicked a button!')

e = name(root)

root.mainloop()