from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')

# root.filename = filedialog.askopenfilename(initialdir='./images', title='Select A File', filetypes=(('png files','*.png'),('all files','*.*')))
# my_label = Label(root, text=root.filename).pack()
# my_img = ImageTk.PhotoImage(Image.open(root.filename))
# my_imageLabel = Label(root, image=my_img).pack()

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir='./images', title='Select A File', filetypes=(('png files','*.png'),('all files','*.*')))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_imageLabel = Label(root, image=my_img).pack()
    

my_btn = Button(root, text='Open File', command=open).pack()
mainloop()