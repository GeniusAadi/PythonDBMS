import mysql.connector as mc

# Connect to the MySQL database
mydb = mc.connect(host="localhost",user="root",password="Genius@5499",database="school",auth_plugin="mysql_native_password")
mycursor = mydb.cursor()

# Function to list all tables in the database
def tab_lst():
    mycursor.execute("SHOW TABLES;")
    tables = mycursor.fetchall()
    for table in tables:
        print(table[0])

# Function to display the content of a table
def content():
    table_name = input("Enter table name: ")
    mycursor.execute(f"SELECT * FROM {table_name};")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

# Function to create a new table
def crt():
    table_name = input("Enter table name: ")
    num_columns = int(input("Enter the number of columns: "))
    columns = []
    for i in range(num_columns):
        column_info = input("Enter column name and data type (e.g., column_name INT) and any key specifications (e.g., INT PRIMARY KEY): ")
        columns.append(column_info)
    column_str = ", ".join(columns)
    mycursor.execute(f"CREATE TABLE {table_name} ({column_str});")
    print("Congratulations! You have successfully created the table.")

# Function to fill data in the table
def entr():
    table_name = input("Enter table name: ")
    mycursor.execute(f"DESC {table_name};")
    columns = mycursor.fetchall()
    column_names = [col[0] for col in columns]
    values = []

    for column in column_names:
        value = input(f"Enter value for the column {column}: ")
        values.append(value)

    value_str = ", ".join(["'" + value + "'" for value in values])
    mycursor.execute(f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({value_str});")
    print("Congratulations! You have successfully filled data in the table.")

# Function to update the table
def updt():
    table_name = input("Enter table name: ")
    num_columns = int(input("Enter number of columns to update: "))
    columns = []
    values = []

    for i in range(num_columns):
        column = input("Enter column name to update: ")
        value = input(f"Enter new value for the column {column}: ")
        columns.append(column)
        values.append(value)

    condition_column = input("Enter column name for condition: ")
    condition_value = input("Enter value for condition: ")
    set_statements = [f"{col} = '{val}'" for col, val in zip(columns, values)]
    set_clause = ", ".join(set_statements)

    mycursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = '{condition_value}';")
    print("Congratulations! You have successfully updated data in the table.")

# Function to delete a row in the table
def dlt_row():
    table_name = input("Enter table name: ")
    condition_column = input("Enter column name for condition: ")
    condition_value = input("Enter value for condition: ")
    mycursor.execute(f"DELETE FROM {table_name} WHERE {condition_column} = '{condition_value}';")
    print("Congratulations! You have successfully deleted data in the table.")

# Function to add a new column in the table
def new_col():
    table_name = input("Enter table name: ")
    column = input("Enter new column name with data type: ")
    mycursor.execute(f"ALTER TABLE {table_name} ADD {column};")
    print("Congratulations! You have successfully added a new column in the table.")

# Function to delete a column in the table
def del_col():
    table_name = input("Enter table name: ")
    column = input("Enter column name to delete: ")
    mycursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column};")
    print("Congratulations! You have successfully deleted the column in the table.")

# Function to delete the table
def del_tab():
    table_name = input("Enter table name: ")
    mycursor.execute(f"DROP TABLE {table_name};")
    print("Congratulations! You have successfully deleted the table.")

# Function to clear the table's items
def clr_tab():
    table_name = input("Enter table name: ")
    mycursor.execute(f"DELETE FROM {table_name};")
    print("Congratulations! You have successfully cleared all the contents in the table.")

# Calling all the functions as per the user required
ans="y"
while ans in ("y","Y","Yes"):
    opt=int(input('''1.Table list
2.Create new table
3.See table content
4.Data entry in the table
5.Add new column in the table
6.Update data in the table
7.Delete a row from table
8.Delete a column from table
9.Clear all the data from the table
10.Delete the table
    Action to perform= '''))
    if opt==1:
        tab_lst()
    elif opt==2:
        crt()
    elif opt==3:
        content()
    elif opt==4:
        entr()
    elif opt==5:
        new_col()
    elif opt==6:
        updt()
    elif opt==7:
        dlt_row()
    elif opt==8:
        del_col()
    elif opt==9:
        clr_tab()
    elif opt==10:
        del_tab()
    else:
        print("Please choose correct option among given options!")
    ans=input("Again?(y/n):")

# Commit the changes and close the connection
mydb.commit()
mycursor.close()
mydb.close()
