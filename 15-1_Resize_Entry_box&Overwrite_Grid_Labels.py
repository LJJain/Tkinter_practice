from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

# def myDelete():
#     lab_1.grid_forget()   # method 1
#     # lab_1.destroy() # method 2

#     btn_1['state'] = NORMAL
#     btn_delete['state'] = DISABLED

lab_1 = Label(root)

def myClick():
    global lab_1
    lab_1.grid_forget()
    
    hello = "Hello " + e.get()
    lab_1 = Label(root, text=hello)
    lab_1.grid(row=3, column=0, pady=10)
    e.delete(0, END)
    # btn_1['state'] = DISABLED
    # btn_delete['state'] = NORMAL


e = Entry(root, width=17, font=('Times New Roman', 24)) # 利用font size 改變輸入框的高度
e.grid(row=0,column=0, padx=10, pady=10)

btn_1 = Button(root, text='Enter Your Name', command=myClick)
btn_1.grid(row=1,column=0, pady=10)
# btn_delete = Button(root, text='Delete Text', command=myDelete)
# btn_delete.grid(row=2,column=0, pady=10)

root.mainloop()