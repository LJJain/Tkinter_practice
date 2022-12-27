from tkinter import *

root = Tk()
root.title('Learn To Code Tkinter')
# 視窗 icon
# root.iconbitmap('icon file')

# r = IntVar()
# r.set("2")

# 多選項時，用loop建立
MODES = [
    ('Pepperoni', 'Pepperoni'),
    ('Cheese', 'Cheese'),
    ('Mushrooms', 'Mushrooms'),
    ('Onion', 'Onion'),
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()

def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# 單選物件 Radio Button
# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda:click(r.get())).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda:click(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text='Click Me !', command=lambda:click(pizza.get()))
myButton.pack()

root.mainloop()