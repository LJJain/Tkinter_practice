from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Image Viewer')
# root.iconbitmap('')

my_img1 = ImageTk.PhotoImage(Image.open('images/book.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/cart.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/headphones.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/rose_coffee.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/shirt.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def next(image_number):
    global my_label
    global btn_next
    global btn_back

    my_label.grid_forget()  #把先前的圖片消失
    my_label = Label(image=image_list[image_number-1])
    btn_next = Button(root, text='>>', command=lambda:next(image_number+1))
    btn_back = Button(root, text='<<', command=lambda:back(image_number-1))
    
    if image_number == len(image_list):
        btn_next = Button(root, text='>>', state=DISABLED)

    btn_back.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text ='Image '+str(image_number)+'of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global btn_next
    global btn_back

    my_label.grid_forget()  #把先前的圖片消失
    my_label = Label(image=image_list[image_number-1])
    btn_next = Button(root, text='>>', command=lambda:next(image_number+1))
    btn_back = Button(root, text='<<', command=lambda:back(image_number-1))
    
    if image_number == 1:
        btn_back = Button(root, text='<<', state=DISABLED)

    btn_back.grid(row=1, column=0)
    btn_next.grid(row=1, column=2)
    my_label.grid(row=0, column=0, columnspan=3) 

    status = Label(root, text ='Image '+str(image_number)+'of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

btn_back = Button(root, text='<<', command=lambda:back(), state=DISABLED)
btn_exit = Button(root, text='EXIT PROGRAM', command=root.quit)
btn_next = Button(root, text='>>', command=lambda:next(2))

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_next.grid(row=1, column=2)

root.mainloop()