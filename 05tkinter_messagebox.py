from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Learn To Code Tkinter')
# 視窗 icon
# root.iconbitmap('icon file')

#  showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno('This is my Popup!', 'Hello world!') # ('Title', 'Message')
    # Label(root=response).pack()
    if response == 1:
        Label(root, text='You Click YES !').pack()
    else:
        Label(root, text='You Click NO !').pack()

Button(root, text='Popup', command=popup).pack()

root.mainloop()