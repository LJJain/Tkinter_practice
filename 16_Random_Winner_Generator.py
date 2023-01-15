from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

def pick():
    entries = ['Sanbid Roy', 'The refuge Malik', 'Google India']
    # convert to a set (確保沒有重複的選項)
    set_entries = set(entries)
    # convert back to list (轉回 List)
    uni_entries = list(set_entries)
    # create a random number between 0 and len(set_entries)
    our_number = len(uni_entries)-1
    rand = randint(0, our_number)


    lab_winner = Label(root, text=uni_entries[rand], font=('Times New Roman', 18)).pack(pady=50)



lab_top = Label(root, text='Win-O-Rama', font=('Times New Roman', 24)).pack(pady=20)

btn_win = Button(root, text='PICK OUT WINNER !!!', font=('Times New Roman',24), command=pick).pack(pady=20)


root.mainloop()