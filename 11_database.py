from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x400')

# Databases

# Create database or connect to one
conn = sqlite3.connect('address_book.db')

# Create Cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
        """)
'''
#  Submit Function For Database
def submit():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Insert Into Table
    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
            })

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()


    # Clear The Text Box
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Query Function
def query():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Query The Database
    c.execute('SELECT *, oid FROM addresses')
    records = c.fetchall()    # 獲取全部
    # print(records)

    # Loop Through Results
    print_records = ''
    for record in records:
        print_records += str(record[0])+ ' ' + str(record[1]) + ' \t' + str(record[6]) + '\n'

    lab_query = Label(root, text=print_records).grid(row=8, column=0, columnspan=2)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

#  Delete Record
def delete():
    # Create database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Cursor
    c = conn.cursor()

    # Delete Record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    
    delete_box.delete(0, END)

    # Commit Changes
    conn.commit()
    # Close Connection
    conn.close()

# Text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30).grid(row=9, column=1)

# Create text Box Labels
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text='ID Number').grid(row=9, column=0)

# Submit Button
btn_submit = Button(root, text='Add Record To Database', command=submit).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#  Query Button
btn_query = Button(root, text='Show Records', command=query).grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Delete Button
btn_delete = Button(root, text='Delete Record', command=delete).grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()