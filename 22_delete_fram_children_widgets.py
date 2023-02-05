from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')


class name:
    def __init__(self, main):
        # self.frame = Frame(main)
        # self.frame.pack()
        self.main = main
        mymenu = Menu(main)
        main.config(menu=mymenu)

        #  Menu Item
        file_menu = Menu(mymenu)
        mymenu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='New...', command=self.FileNew)
        file_menu.add_separator()   # 添加分隔線
        file_menu.add_command(label='Exit', command=main.quit)

        # Create an Edit Menu Item
        edit_menu = Menu(mymenu)
        mymenu.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='Cut', command=self.EditCut)
        edit_menu.add_command(label='Copy', command=self.our_command)

        # Create an Option Menu Item
        option_menu = Menu(mymenu)
        mymenu.add_cascade(label='Option', menu=option_menu)
        option_menu.add_command(label='Find', command=self.our_command)
        option_menu.add_command(label='Find Next', command=self.our_command)

        # Create some frames
        self.file_new_frame = Frame(main, width=400, height=400, bg='red')
        self.edit_cut_frame = Frame(main, width=400, height=400, bg='blue')

    def our_command(self):
        lab_1 = Label(self.main, text='You Clicked a Dropdown Menu!').pack()

    def FileNew(self):
        self.HideAllFrame()
        self.file_new_frame.pack(fill='both', expand=1)
        lab_1 = Label(self.file_new_frame, text='You Clicked the file >> New >> New Menu').pack()

    def EditCut(self):
        self.HideAllFrame()
        self.edit_cut_frame.pack(fill='both', expand=1)
        lab_1 = Label(self.edit_cut_frame, text='You Clicked the file >> Edit >> Cut Menu').pack()

        label_child = Label(self.edit_cut_frame, text=self.edit_cut_frame.winfo_children())
        label_child.pack(pady=10)

    def HideAllFrame(self):
        # Loop thru all the children and delete them
        for widget in self.file_new_frame.winfo_children():
            widget.destroy()

        for widget in self.edit_cut_frame.winfo_children():
            widget.destroy()

        self.file_new_frame.pack_forget()
        self.edit_cut_frame.pack_forget()



e = name(root)
root.mainloop()