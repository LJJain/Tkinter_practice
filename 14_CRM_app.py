from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import csv

root = Tk()
root.title('Learn To Code Tkinter')
# root.iconbitmap('icon file')
root.geometry('400x600')

conn = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'Egg790508~',
        database= 'db_test',
    )
# print(conn)

# Create a cursor and initialize it
cursor = conn.cursor()
# Create database
# cursor.execute("CREATE DATABASE db_test")
# Test to see if database exists
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)

# Create Tabel
cursor.execute("CREATE TABLE IF NOT EXISTS customers(first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(10),price_paid DECIMAL(10, 2),user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter Table
'''
cursor.execute("ALTER TABLE customers ADD (\
    email VARCHAR(255),\
    address_1 VARCHAR(255),\
    address_2 VARCHAR(255),\
    city VARCHAR(50),\
    state VARCHAR(50),\
    country VARCHAR(255),\
    phone VARCHAR(255),\
    payment_method VARCHAR(50),\
    discount_code VARCHAR(255)\
    )")
'''

# Show Talbel
# cursor.execute("SELECT * FROM customers")
# # print(cursor.description)
# for thing in cursor.description:
#     print(thing)

# Clear Text Fields
def clearFields():
    box_first_name.delete(0, END)
    box_last_name.delete(0, END)
    box_address1.delete(0, END)
    box_address2.delete(0, END)
    box_city.delete(0, END)
    box_state.delete(0, END)
    box_zipcode.delete(0, END)
    box_country.delete(0, END)
    box_phone.delete(0, END)
    box_email.delete(0, END)
    # box_username.delete(0, END)
    box_payment_method.delete(0, END)
    box_discount_code.delete(0, END)
    box_pricepaid.delete(0, END)

# Submit Customer To Database
def addCustomer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (box_first_name.get(), box_last_name.get(), box_zipcode.get(), box_pricepaid.get(), box_email.get(), box_address1.get(), box_address2.get(), box_city.get(), box_state.get(), box_country.get(), box_phone.get(), box_payment_method.get(), box_discount_code.get())
    cursor.execute(sql_command, values)

    # commit the changes to database
    conn.commit()
    # clear the fields
    clearFields()

# Write To CSV Function
def writeToCsv(result):
    with open('customer.csv', 'w', newline='') as f:    # newline='' 避免產生空的row(格行新增)
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

# Search Customer
def searchCustomer():
    search_customers = Tk()
    search_customers.title('Search Customers')
    search_customers.geometry('1024x768')
    
    def searchNow():
        selected = drop.get()
        sql = ''
        if selected == 'Search by ...':
            test = Label(search_customers, text='Hey! You forgot to pick a drop down selection.').grid(row=2, column=0, columnspan=2)
        if selected == 'Last Name':
            sql = "SELECT * FROM customers WHERE last_name = %s"
            
        if selected == 'Email Address':
            sql = "SELECT * FROM customers WHERE email = %s"
            
        if selected == 'Customer ID':
            sql = "SELECT * FROM customers WHERE user_id = %s"
            
        
        searched = box_search.get()
        # sql = "SELECT * FROM customers WHERE last_name = %s"
        name = (searched, )
        result = cursor.execute(sql, name)
        result = cursor.fetchall()

        if not result:
            result = "Record not found ..."
            lab_search = Label(search_customers, text=result).grid(row=2, column=0, columnspan=2)
        # print(result)
        else:
            for index, x in enumerate(result):
                num = 0
                index += 3
                for y in x:
                    lab_search = Label(search_customers, text=y).grid(row=index, column=num)
                    num += 1
            btn_csv = Button(search_customers, text='Save as CSV', command=lambda: writeToCsv).grid(row=index+3, column=0) 
        # lab_search = Label(search_customers, text=result).grid(row=3, column=0, padx=10, columnspan=2)
        


    # Entry box to search for customer
    box_search = Entry(search_customers)
    box_search.grid(row=0, column=1, padx=10, pady=10)
    # Entry box label search for customer
    lab_search_box = Label(search_customers, text='Search').grid(row=0, column=0, padx=10, pady=10)
    # Entry box Button
    btn_search_box = Button(search_customers, text='Search', command=searchNow).grid(row=1, column=0, padx=10)
    drop = ttk.Combobox(search_customers, value=['Search by ...', 'Last Name', 'Email Address', 'Customer ID'])
    drop.current(0)
    drop.grid(row=0, column=2)


# List Customers
def ListCustomers():
    list_customer_query = Tk()
    list_customer_query.title('List All Customers')
    list_customer_query.geometry('800x600')
    # Query The Database
    cursor.execute("SELECT * FROM customers")
    result = cursor.fetchall()
    
    for index,x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customer_query, text=y).grid(row=index, column=num)
            num += 1

    btn_csv = Button(list_customer_query, text='Save as CSV', command=lambda: writeToCsv(result)).grid(row=index+1, column=0)

# Create a Label
lab_title = Label(root, text='Customer Database', font=('Times New Roman', 16)).grid(row=0, column=0, columnspan=2, pady=10)

lab_first_name = Label(root, text='First Name').grid(row=1, column=0, sticky=W, padx=10)
lab_last_name = Label(root, text='Last Name').grid(row=2, column=0, sticky=W, padx=10)
lab_address1 = Label(root, text='Address 1').grid(row=3, column=0, sticky=W, padx=10)
lab_address2 = Label(root, text='Address 2').grid(row=4, column=0, sticky=W, padx=10)
lab_city = Label(root, text='City').grid(row=5, column=0, sticky=W, padx=10)
lab_state = Label(root, text='State').grid(row=6, column=0, sticky=W, padx=10)
lab_zipcode = Label(root, text='Zip Code').grid(row=7, column=0, sticky=W, padx=10)
lab_country = Label(root, text='Country').grid(row=8, column=0, sticky=W, padx=10)
lab_phone = Label(root, text='Phone').grid(row=9, column=0, sticky=W, padx=10)
lab_email = Label(root, text='Email').grid(row=10, column=0, sticky=W, padx=10)
# lab_username = Label(root, text='Username').grid(row=11, column=0, sticky=W, padx=10)
lab_payment_method = Label(root, text='Payment Method').grid(row=11, column=0, sticky=W, padx=10)
lab_discount_code = Label(root, text='Discount Code').grid(row=12, column=0, sticky=W, padx=10)
lab_pricepaid = Label(root, text='Pricepaid').grid(row=13, column=0, sticky=W, padx=10)

# Create Entry Boxes
box_first_name = Entry(root)
box_first_name.grid(row=1, column=1, pady=5)
box_last_name = Entry(root)
box_last_name.grid(row=2, column=1, pady=5)
box_address1 = Entry(root)
box_address1.grid(row=3, column=1, pady=5)
box_address2 = Entry(root)
box_address2.grid(row=4, column=1, pady=5)
box_city = Entry(root)
box_city.grid(row=5, column=1, pady=5)
box_state = Entry(root)
box_state.grid(row=6, column=1, pady=5)
box_zipcode = Entry(root)
box_zipcode.grid(row=7, column=1, pady=5)
box_country = Entry(root)
box_country.grid(row=8, column=1, pady=5)
box_phone = Entry(root)
box_phone.grid(row=9, column=1, pady=5)
box_email = Entry(root)
box_email.grid(row=10, column=1, pady=5)
# box_username = Entry(root)
# box_username.grid(row=11, column=1, pady=5)
box_payment_method = Entry(root)
box_payment_method.grid(row=11, column=1, pady=5)
box_discount_code = Entry(root)
box_discount_code.grid(row=12, column=1, pady=5)
box_pricepaid = Entry(root)
box_pricepaid.grid(row=13, column=1, pady=5)

# Create Buttons
btn_add_customer = Button(root, text='Add Custom', command=addCustomer).grid(row=14, column=0, padx=10, pady=10)
btn_clear_fields = Button(root, text='Clear Fields', command=clearFields).grid(row=14, column=1)
# list customer buttons
btn_list_customers = Button(root, text='List Customer', command=ListCustomers).grid(row=15, column=0, sticky=W, padx=10)
# Search Customer buttons
btn_search_customers = Button(root, text='Search Customer', command=searchCustomer).grid(row=15, column=1, sticky=W, padx=10)

root.mainloop()