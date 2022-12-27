from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=50, borderwidth=5, font=(20))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def buttonNum(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_num)
    e.delete(0, END)

def buttonMinus():
    first_num = e.get()
    global f_num
    global math
    math = 'subtaction'
    f_num = float(first_num)
    e.delete(0, END)

def buttonMultiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_num)
    e.delete(0, END)

def buttonDivide():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_num)
    e.delete(0, END)

def buttonEqual():
    second_num = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + float(second_num))
    
    if math == 'subtaction':
        e.insert(0, f_num - float(second_num))
    
    if math == 'multiplication':
        e.insert(0, f_num * float(second_num))

    if math == 'division':
        e.insert(0, f_num / float(second_num))

    


# Buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: buttonNum(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: buttonNum(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: buttonNum(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: buttonNum(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: buttonNum(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: buttonNum(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: buttonNum(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: buttonNum(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: buttonNum(9))
button_0 = Button(root, text='0', padx=90, pady=20, command=lambda: buttonNum(0))
button_dot = Button(root, text='.', padx=40, pady=20, command=lambda: buttonNum('.'))

button_equal = Button(root, text='=', padx=130, pady=20, command=buttonEqual)
button_clear = Button(root, text='Clear', padx=40, pady=20, command=buttonClear)
button_add = Button(root, text='+', padx=40, pady=20, command=buttonAdd)
button_minus = Button(root, text='-', padx=40, pady=20, command=buttonMinus)
button_multiply = Button(root, text='*', padx=40, pady=20, command=buttonMultiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=buttonDivide)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0, columnspan=2)
button_dot.grid(row=4, column=2)

button_equal.grid(row=5, column=0, columnspan=3)
button_clear.grid(row=1, column=3)
button_add.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_divide.grid(row=5, column=3)

root.mainloop()