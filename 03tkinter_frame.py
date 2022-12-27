from tkinter import *

root = Tk()
root.title('Learn To Code Tkinter')
# 視窗 icon
# root.iconbitmap('icon file')

# 創建框架
frame= LabelFrame(root, text='This is my frame...', padx=50, pady=50) # 框架內部的padding
frame.pack(padx=100, pady=100)    #框架外的padding

# 建立物件放入框架
b = Button(frame, text="Don't Click here")
b2 = Button(frame, text="Don't Click here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()