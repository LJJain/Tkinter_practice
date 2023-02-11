from tkinter import *
# from PIL import ImageTk, Image

def App():
    root = Tk()
    root.title('Learn To Code Tkinter')
    # root.iconbitmap('icon file')
    root.geometry('400x400')

    app = Main(root)
    root.mainloop()

class Main():
    def __init__(self, main):
        self.main = main
        self.fram_listbox = Frame(self.main)
        self.fram_listbox.pack()

        self.scrollbar = Scrollbar(self.fram_listbox, orient=VERTICAL)
        self.listbox = Listbox(self.fram_listbox, width=50, yscrollcommand=self.scrollbar.set, selectmode=EXTENDED)
        # selectmode: SINGLE=單選, BROWSE= , MULTIPLE=多選(直接), EXTENDED=多選
        # Configure the scrollbar
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.pack(pady=15)

        # Add the items to the listbox
        self.listbox.insert(END, 'this is an item !')
        self.listbox.insert(0, 'Second Item !')

        # Add list of items
        list = ['One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four', 'One', 'Two', 'Three', 'Four']
        for item in list:
            self.listbox.insert('end', item)

        self.frame_btn = Frame(self.main)
        self.frame_btn.pack()
        
        self.button_delete = Button(self.frame_btn, text='Delete', command=self.Delete)
        self.button_delete.pack(pady=10)

        self.button_select = Button(self.frame_btn, text='Select', command=self.Select)
        self.button_select.pack(pady=10)

        self.button_delete_all = Button(self.frame_btn, text='Delete All', command=self.DeleteAll)
        self.button_delete_all.pack(pady=10)

        self.button_delete_multiple = Button(self.frame_btn, text='Delete Multiple', command=self.DeleteMultiple)
        self.button_delete_multiple.pack(pady=10)

        self.button_select_all = Button(self.frame_btn, text='Select All', command=self.SelectAll)
        self.button_select_all.pack(pady=10)

        self.label = Label(self.frame_btn, text='')
        self.label.pack(pady=5)

    def Delete(self):
        self.listbox.delete(ANCHOR) # ANCHOR 當前指向物件
        self.label.config(text='')

    def Select(self):
        self.label.config(text=self.listbox.get(ANCHOR))

    def DeleteAll(self):
        self.listbox.delete(0, END)

    def DeleteMultiple(self):
        for item in reversed(self.listbox.curselection()):
            self.listbox.delete(item)
        self.label.config(text='')

    def SelectAll(self):
        result=''
        for item in self.listbox.curselection():
            result = result + str(self.listbox.get(item)) + '\n'

        self.label.config(text=result)







if __name__ == '__main__':
    App()