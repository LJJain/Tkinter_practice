from tkinter import *
from PIL import ImageTk, Image

def App():
    root = Tk()
    root.title('Learn To Code Tkinter')
    # root.iconbitmap('icon file')
    root.geometry('700x500')

    app = Main(root)
    root.mainloop()

class Main():
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.my_entries = []
        # Row Loop
        for y in range(5):
            # column loop
            for x in range(5):
                self.entries = Entry(self.frame)
                self.entries.grid(row=y, column=x, padx=5, pady=10)
                self.my_entries.append(self.entries)
        
        button = Button(self.frame, text='Click Me', command=self.Something)
        button.grid(row=6, column=0, pady=20)

        self.label = Label(self.frame, text='')
        self.label.grid(row=7, column=0, pady=10)
        
    def Something(self):
        entry_list = ''
        for entry in self.my_entries:
            entry_list = entry_list + str(entry.get()) + '\n'
            self.label.config(text=entry_list)

if __name__ == '__main__':
    App()