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
        # Panels
        panel_1 = PanedWindow(bd=4, relief='raised', bg='red')
        panel_1.pack(fill=BOTH, expand=1)

        left_label = Label(panel_1, text='Left Panel')
        panel_1.add(left_label)

        # Create Second Panel
        panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief='raised', bg='Blue')
        panel_1.add(panel_2)

        top = Label(panel_2, text='Top Panel')
        panel_2.add(top)

        bottom = Label(panel_2, text='Bottom Panel')
        panel_2.add(bottom)

e = name(root)
root.mainloop()