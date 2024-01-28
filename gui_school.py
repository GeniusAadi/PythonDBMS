import mysql.connector as mc
import tkinter as tk

# Connect to the MySQL database
# Function to connect to the MySQL database
def connect_db():
    try:
        db_params = DataBase_name_passwd.get()
        db_name, db_passwd = db_params.split(",")
        connection = mc.connect(
            host="localhost",
            user="root",
            password=db_passwd,
            database=db_name,
            auth_plugin="mysql_native_password"
        )
        success_text=tk.Text(app,fg="white",bg="orange")
        success_text.delete(1.0, tk.END)
        success_text.insert(tk.END, "Congratulations! You have successfully connected to the database.")
        success_text.place(x=170,y=110,height=95,width=415)
        success_text.config(state=tk.DISABLED)
        return connection
    except mc.Error as e:
        error_text=tk.Text(app,fg="white",bg="orange")
        error_text.delete(1.0, tk.END)
        error_text.insert(tk.END, f"Error: {str(e)}")
        error_text.place(x=170,y=110,height=95,width=415)
        error_text.config(state=tk.DISABLED)
        return None

#window for gui
app = tk.Tk()
app.title("Database Manager")
app.geometry("590x210")
app.configure(background="purple")

#Function for User input
def user_input():
    global table_name,column_info,column,value,condition_for_column,condition_for_value,DataBase_name_passwd
    frame = tk.Frame(app, relief=tk.SUNKEN, borderwidth=2)
    frame.place(x=0, y=0, height=210, width=150)
    DataBase_name_passwd=tk.Entry(frame,fg="blue",bg="light green")
    DataBase_name_passwd.insert(0,"DataBase,Passwd")
    DataBase_name_passwd.bind("<FocusIn>", lambda event: clear_placeholder(event, DataBase_name_passwd, "DataBase,Passwd"))  # Bind event to clear placeholder on focus
    DataBase_name_passwd.bind("<FocusOut>", lambda event: restore_placeholder(event, DataBase_name_passwd, "DataBase,Passwd"))
    DataBase_name_passwd.place(x=0,y=0,height=30,width=150)
    table_name=tk.Entry(frame,fg="blue",bg="light green")
    table_name.insert(0,"table name")
    table_name.bind("<FocusIn>", lambda event: clear_placeholder(event, table_name, "table name"))  # Bind event to clear placeholder on focus
    table_name.bind("<FocusOut>", lambda event: restore_placeholder(event, table_name, "table name"))
    table_name.place(x=0,y=30,height=30,width=150)
    column_info=tk.Entry(frame,fg="blue",bg="light green")
    column_info.insert(0,"column data_type key")
    column_info.bind("<FocusIn>", lambda event: clear_placeholder(event, column_info, "column data_type key"))  # Bind event to clear placeholder on focus
    column_info.bind("<FocusOut>", lambda event: restore_placeholder(event, column_info, "column data_type key"))
    column_info.place(x=0,y=60,height=30,width=150)
    column=tk.Entry(frame,fg="blue",bg="light green")
    column.insert(0,"column_name")
    column.bind("<FocusIn>", lambda event: clear_placeholder(event, column, "column_name"))  # Bind event to clear placeholder on focus
    column.bind("<FocusOut>", lambda event: restore_placeholder(event, column, "column_name"))
    column.place(x=0,y=90,height=30,width=150)
    value=tk.Entry(frame,fg="blue",bg="light green")
    value.insert(0,"value")
    value.bind("<FocusIn>", lambda event: clear_placeholder(event, value, "value"))  # Bind event to clear placeholder on focus
    value.bind("<FocusOut>", lambda event: restore_placeholder(event, value, "value"))
    value.place(x=0,y=120,height=30,width=150)
    condition_for_column=tk.Entry(frame,fg="blue",bg="light green")
    condition_for_column.insert(0,"column_name_for_condition")
    condition_for_column.bind("<FocusIn>", lambda event: clear_placeholder(event, condition_for_column, "column_name_for_condition"))  # Bind event to clear placeholder on focus
    condition_for_column.bind("<FocusOut>", lambda event: restore_placeholder(event, condition_for_column, "column_name_for_condition"))
    condition_for_column.place(x=0,y=150,height=30,width=150)
    condition_for_value=tk.Entry(frame,fg="blue",bg="light green")
    condition_for_value.insert(0,"value_for_condition")
    condition_for_value.bind("<FocusIn>", lambda event: clear_placeholder(event, condition_for_value, "value_for_condition"))  # Bind event to clear placeholder on focus
    condition_for_value.bind("<FocusOut>", lambda event: restore_placeholder(event, condition_for_value, "value_for_condition"))
    condition_for_value.place(x=0,y=180,height=30,width=150)

# Create a function to clear the placeholder text when the Entry widget receives focus
def clear_placeholder(event,x,placeholder_text):
    if x.get() == placeholder_text:
        x.delete(0, tk.END)

# Create a function to restore the placeholder text if the Entry widget is empty when it loses focus
def restore_placeholder(event,x,placeholder_text):
    if not x.get():
        x.insert(0, placeholder_text)

user_input()

# Function to list all tables in the database
def tab_lst():
    global table_list
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES;")
    tables = mycursor.fetchall()
    table_list = tk.Text(app,bg="orange",fg="white")
    table_list.delete(1.0, tk.END)  # Clear the text widget
    for table in tables:
        table_list.insert(tk.END, table[0] + "\n")
    table_list.place(x=170,y=110,height=95,width=415)
    table_list.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to display the content of a table
def content():
    data=table_name.get()
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {data};")
    rows = mycursor.fetchall()
    content_text=tk.Text(app,bg="orange",fg="white")
    content_text.delete(1.0, tk.END)  # Clear the text widget
    for row in rows:
        content_text.insert(tk.END, str(row) + "\n")
    content_text.place(x=170,y=110,height=95,width=415)
    content_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to create a new table
def create_table():
    mydb = connect_db()
    mycursor = mydb.cursor()
    data1=table_name.get()
    data3=column_info.get()
    mycursor.execute(f"CREATE TABLE {data1} ({data3});")
    success_text=tk.Text(app,bg="orange",fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully created the table.")
    success_text.place(x=170,y=110,height=95,width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to fill data in the table
def entr():
    data1=table_name.get()
    data2=value.get()
    mydb = connect_db()
    mycursor = mydb.cursor()
    data = data2.split(',')
    for i in data:
        if i.isdigit():
            index_to_replace = data.index(i)
            data[index_to_replace] = int(i)
    tpl = tuple(data)  # Move this line outside the try block
    try:
        # Construct the SQL query string with placeholders
        print(f"Inserting data into {data1} with values: {tpl}") # Debugging message
        query = f"INSERT INTO {data1} VALUES {tpl}"
        print(f"Executing query: {query}") # Debugging message
        # Execute the query with the data
        mycursor.execute(query)
        success_text = tk.Text(app, bg="orange", fg="white")
        success_text.delete(1.0, tk.END)
        success_text.insert(tk.END, "Congratulations! You have successfully filled data in the table.")
        success_text.place(x=170, y=110, height=95, width=415)
        success_text.config(state=tk.DISABLED)
    except Exception as e:
        error_text = tk.Text(app, bg="red", fg="white")
        error_text.delete(1.0, tk.END)
        error_text.insert(tk.END, f"Error: {str(e)}")
        error_text.place(x=170, y=110, height=95, width=415)
        error_text.config(state=tk.DISABLED)
        print(f"Error: {str(e)}") # Debugging message
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to update the table
def updt():
    data1=table_name.get()
    data2=column.get()
    data3=value.get()
    data4=condition_for_column.get()
    data5=condition_for_value.get()
    query=f"UPDATE {data1} SET {data2} = {data3} WHERE {data4} = '{data5}'"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully updated data in the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to delete a row in the table
def dlt_row():
    data1=table_name.get()
    data2=condition_for_column.get()
    data3=condition_for_value.get()
    query=f"DELETE FROM {data1} WHERE {data2} = '{data3}'"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully deleted the row from the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to add a new column in the table
def new_col():
    data1=table_name.get()
    data2=column.get()
    query=f"ALTER TABLE {data1} ADD {data2}"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully added new column in the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to delete a column in the table
def del_col():
    data1=table_name.get()
    data2=column.get()
    query=f"ALTER TABLE {data1} DROP COLUMN {data2}"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully deleted the column from the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

#Function to describe a table
def desc_tab():
    data1=table_name.get()
    mydb=connect_db()
    mycursor=mydb.cursor()
    query=f"DESC {data1}"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    content_text=tk.Text(app,bg="orange",fg="white")
    content_text.delete(1.0, tk.END)  # Clear the text widget
    for row in rows:
        content_text.insert(tk.END, str(row) + "\n")
    content_text.place(x=170,y=110,height=95,width=415)
    content_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to clear the table's items
def clr_tab():
    data=table_name.get()
    query=f"DELETE FROM {data}"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully cleared the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()

# Function to delete the table
def del_tab():
    data=table_name.get()
    query=f"DROP TABLE {data}"
    mydb = connect_db()
    mycursor = mydb.cursor()
    mycursor.execute(query)
    success_text = tk.Text(app, bg="orange", fg="white")
    success_text.delete(1.0, tk.END)
    success_text.insert(tk.END, "Congratulations! You have successfully deleted the table.")
    success_text.place(x=170, y=110, height=95, width=415)
    success_text.config(state=tk.DISABLED)
    mydb.commit()
    mycursor.close()
    mydb.close()


#Button for Connect to data base
database_connect_button=tk.Button(app,text="Connect",command=connect_db,bg="cyan")
database_connect_button.place(x=170,y=0,height=30,width=100)

#Button for table list
list_tables_button = tk.Button(app, text="List Tables", command=tab_lst,bg="cyan")
list_tables_button.place(x=275,y=0,height=30,width=100)

#button to create a table
create_table_button = tk.Button(app, text="Create Table", command=create_table,bg="cyan")
create_table_button.place(x=380,y=0,height=30,width=100)

#button to Describe a table
describe_table_button=tk.Button(app,text="Describe Table",command=desc_tab,bg="cyan")
describe_table_button.place(x=485,y=0,height=30,width=100)

#button to see table content
content_button = tk.Button(app,text="Table Content",command=content,bg="cyan")
content_button.place(x=170,y=35,height=30,width=100)

#button to fill data in the table
data_fill_button = tk.Button(app,text="Fill Data",command=entr,bg="cyan")
data_fill_button.place(x=275,y=35,height=30,width=100)

#button to update data in the table
data_update_button = tk.Button(app,text="Update Data",command=updt,bg="cyan")
data_update_button.place(x=380,y=35,height=30,width=100)

#button to delete row from table
row_delete_button = tk.Button(app,text="Delete Data",command=dlt_row,bg="cyan")
row_delete_button.place(x=485,y=35,height=30,width=100)

#button to add new column in the table
add_column_button = tk.Button(app,text="Add column",command=new_col,bg="cyan")
add_column_button.place(x=170,y=70,height=30,width=100)

#button to delete column
del_column_button = tk.Button(app,text="Delete Column",command=del_col,bg="cyan")
del_column_button.place(x=275,y=70,height=30,width=100)

#button to clear all data from table
clear_data_button=tk.Button(app,text="Clear Table",command=clr_tab,bg="cyan")
clear_data_button.place(x=380,y=70,height=30,width=100)

#button to delete table
table_delete_button=tk.Button(app,text="Delete Table",command=del_tab,bg="cyan")
table_delete_button.place(x=485,y=70,height=30,width=100)

def style_button(button):
    button.configure(bg="cyan", fg="red", relief="raised", borderwidth=3, font=("Helvetica", 10))

button_list = [
    database_connect_button, list_tables_button, create_table_button,
    describe_table_button, content_button, data_fill_button,
    data_update_button, row_delete_button, add_column_button,
    del_column_button, clear_data_button, table_delete_button
]

for button in button_list:
    style_button(button)

#closing gui window
app.mainloop()