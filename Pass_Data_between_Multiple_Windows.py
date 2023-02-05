from tkinter import *

class Main:
    def __init__(self, main):
        self.frame = Frame(main)

        btn = Button(self.frame, text='Open Settings', command=self.open)
        btn.pack()

        self.label = Label(self.frame, text='')
        self.label.pack(pady=10)

        self.frame.pack(padx=10, pady=10)

    def open(self):
        settingsWindow =SettingsWindow(self.update)

    def update(self, input, option):
        print('Update function from Main Window')
        print('Entry Value:', input)
        print('Radio Option:', option)
        self.label.configure(text= input + str(option))

class SettingsWindow:
    def __init__(self, update):
        top = Toplevel()
        self.frame = Frame(top)
        self.update = update

        self.input = StringVar()
        entry = Entry(top, textvariable=self.input)
        entry.pack(padx=10, pady=10)

        self.option = IntVar()
        option1 = Radiobutton(top, value=1, text='option 1', variable=self.option)
        option1.pack(padx=10, pady=10)
        option2 = Radiobutton(top, value=2, text='option 2', variable=self.option)
        option2.pack(padx=10, pady=10)

        btn = Button(top, text='Submit', command=self.submit)
        btn.pack()

        self.frame.pack(padx=10, pady=10)

    def submit(self):
        self.update(self.input.get(), self.option.get())

root = Tk()
main = Main(root)
root.mainloop()