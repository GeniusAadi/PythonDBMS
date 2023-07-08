import mysql.connector as mc
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# auth_plugin is used to avoid authentication plugin is not supported error.
mydb = mc.connect(host="localhost", user="root", password="Genius@5499", database="school", auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

# To create a window
win = tk.Tk(screenName="School Database",baseName="Database",className="Tk",useTk=True,sync=True,use=None)
win.geometry("300x500")
win.title("School Database")
# img=Image.open("C:\\Users\\sandeephjf\\Pictures\\Logo.png")
# bag=ImageTk.PhotoImage(img)
# tk.Label(win,image=bag).grid(row=0,column=0,sticky='W',columnspan=1,rowspan=1,padx=2,pady=2)
win.config(bg="#B23AEE")
frm=ttk.Frame(win,padding=2)
frm.grid()

# To see all the tables
def tab_lst():
    mycursor.execute("show tables;")
    for tab in mycursor:
        txt = tk.Label(text=tab)
        txt.grid()

# To show all the contents inside the table
def cmd():
    table = table_name.get()
    mycursor.execute(f"SELECT * FROM {table};")
    rows = mycursor.fetchall()

    if rows:
        num_columns = len(rows[0])
        num_rows = len(rows)

        # Calculate the required width for each column
        column_width = int(win.winfo_width() / num_columns)

        # Create a frame to hold the treeview and scrollbar
        frame = tk.Frame(win)
        frame.grid(row=1, column=0, sticky="nsew")

        # Create a treeview widget
        tree = ttk.Treeview(frame)
        tree["columns"] = tuple(range(num_columns))

        # Format the columns
        for i in range(num_columns):
            tree.column(i, width=column_width, anchor="center")
            tree.heading(i, text=f"Column {i}")

        # Insert the rows of data into the treeview
        for row in rows:
            tree.insert("", "end", values=row)

        # Configure the scrollbars
        y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=y_scrollbar.set)

        # Pack the treeview widget and scrollbar
        tree.grid(row=0, column=0, sticky="nsew")
        y_scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure grid weights to expand the frame
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        # Calculate the required height for the treeview
        tree_height = min(200, num_rows * 20)  # Set a maximum height of 200 pixels

        # Set the height of the treeview
        tree.configure(height=tree_height)
    else:
        tk.Label(win, text="No data found in the table.").grid(row=1, column=0)

def content():
    global table_name
    tk.Label(text="Table name:").grid()
    table_name = tk.Entry(win)
    table_name.grid(column=1)
    button = tk.Button(win, text="Show", bg="red", fg="black", command=cmd)
    button.grid()

# To create a new table
def crt():
    #getting table name and column from entry
    table_name = table_name_entry.get()
    #Sql command
    mycursor.execute(f"create table {table_name} ({', '.join(columns)});")
    ttk.Label(text="Congratulations! You have successfully created the table.").grid(row=num_columns+3, column=0)
def nxt_btn():
    global num_columns
    #To receive the no. of columns
    num_columns = num_columns_entry.get()

# To fill data in the table
def entr():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(row=2,column=1)
    mycursor.execute(f"desc {table_name.get()};")
    columns = mycursor.fetchall()
    for column in columns:
        tk.Label(text=column[0:2]).grid()
    ttk.Label(text="no. of columns:").grid()
    num = tk.Entry()
    num.grid(column=1)
    lst = []
    for i in range(int(num.get())):
        ttk.Label(text="Fill with respect to column:").grid()
        clm = tk.Entry()
        clm.grid(column=1)
        lst.append(clm.get())
    tpl = ", ".join(lst)
    mycursor.execute(f"insert into {table_name.get()} values ({tpl});")
    tk.Label(master=win,text="Congratulations! You have successfully filled data in the table.").grid()

# To update the table
def updt():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    ttk.Label(text="Column name:").grid()
    col = tk.Entry()
    col.grid(column=1)
    ttk.Label(text="Enter value:").grid()
    val = tk.Entry()
    val.grid(column=1)
    ttk.Label(text="Column name for condition:").grid()
    cond_col = tk.Entry()
    cond_col.grid(column=1)
    ttk.Label(text="Enter value for condition:").grid()
    cond_val = tk.Entry()
    cond_val.grid(column=1)
    mycursor.execute(f"update {table_name.get()} set {col.get()} = {val.get()} where {cond_col.get()} = {cond_val.get()};")
    tk.Label(text="Congratulations! You have successfully updated data in the table.").grid()

# To delete row in the table
def dlt_row():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    ttk.Label(text="Column name for condition:").grid()
    cond_col = tk.Entry()
    cond_col.grid(column=1)
    ttk.Label(text="Enter value for condition:").grid()
    cond_val = tk.Entry()
    cond_val.grid(column=1)
    mycursor.execute(f"delete from {table_name.get()} where {cond_col.get()} = {cond_val.get()};")
    tk.Label(text="Congratulations! You have successfully deleted data in the table.").grid()

# To add a new column in the table
def new_col():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    ttk.Label(text="Column name:").grid()
    col_name = tk.Entry()
    col_name.grid(column=1)
    ttk.Label(text="Data type of column:").grid()
    col_type = tk.Entry()
    col_type.grid(column=1)
    mycursor.execute(f"alter table {table_name.get()} add column {col_name.get()} {col_type.get()};")
    tk.Label(text="Congratulations! You have successfully added a new column in the table.").grid()

# To delete a column in the table
def del_col():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    ttk.Label(text="Column name:").grid()
    col_name = tk.Entry()
    col_name.grid(column=1)
    mycursor.execute(f"alter table {table_name.get()} drop column {col_name.get()};")
    tk.Label(text="Congratulations! You have successfully deleted the column in the table.").grid()

# To delete the table
def del_tab():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    mycursor.execute(f"drop table {table_name.get()};")
    tk.Label(text="Congratulations! You have successfully deleted the table.").grid()

# To clear the table's items
def clr_tab():
    ttk.Label(text="Table name:").grid()
    table_name = tk.Entry()
    table_name.grid(column=1)
    mycursor.execute(f"delete from {table_name.get()};")
    tk.Label(text="Congratulations! You have successfully cleared all the contents in the table.").grid()

def callback(selection):
    global table_name_entry, num_columns_entry, columns, num_columns
    selection = var.get()
    new_var = selection
    tk.Label(text=new_var).grid()
    if new_var == "1.Table list":
        tab_lst()
    elif new_var == "2.Create table":
        #Entry of table name and no. of columns
        ttk.Label(text="Table name:").grid(row=1, column=0)
        table_name_entry = tk.Entry(win)
        table_name_entry.grid(row=1, column=1)
        #No. of columns
        ttk.Label(text="no. of columns:").grid(row=2, column=0)
        num_columns_entry = tk.Entry(win)
        num_columns_entry.grid(row=2, column=1)
        #Button for next
        button_create = tk.Button(win, text="Next", command=nxt_btn)
        button_create.grid(row=3, column=0)
        #Conditions to avoid error
        if num_columns.isdigit():  # Check if num_columns is a valid positive integer
            num_columns = int(num_columns)
            #Entry of columns
            columns = []
            for i in range(num_columns):
                ttk.Label(text=f"Fill column name {i+1} \n along with datatype \n and key if needed:").grid(row=i+2, column=0)
                column_entry = tk.Entry(win)
                column_entry.grid(row=i+2, column=1)
                columns.append(column_entry.get())
        else:
            ttk.Label(text="Error: Please enter a valid number of columns.").grid(row=4, column=0)
        #Button to create
        button_create = tk.Button(win, text="Create Table", command=crt)
        button_create.grid(row=3, column=1)
    elif new_var == "3.Data entry in the table":
        entr()
    elif new_var == "4.Data update in the table":
        updt()
    elif new_var == "5.Data delete from the table":
        dlt_row()
    elif new_var == "6.Add new column in the table":
        new_col()
    elif new_var == "7.See table content":
        content()
    elif new_var == "8.Delete column":
        del_col()
    elif new_var == "9.Delete table":
        del_tab()
    elif new_var == "10.Clear the table content":
        clr_tab()
    else:
        print("Error! Please make a correct choice.")

var = tk.StringVar()
var.set("Choose the option you want to perform:")
slct = ["1.Table list","2.Create table","3.Data entry in the table","4.Data update in the table","5.Data delete from the table","6.Add new column in the table","7.See table content","8.Delete column","9.Delete table","10.Clear the table content"]
option = tk.OptionMenu(win, var, *slct, command=callback)
option.grid(row=0,column=0)
option.config(bg="#FFD700",fg="red")
win.mainloop()
mycursor.close()
mydb.close()
