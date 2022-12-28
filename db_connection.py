import mysql.connector as c

def mysql_connection():
    try:
        connection = c.connect(host = 'localhost',
        user = 'root',
        password = 'Yasin@786'
        )
        create_db_query = "CREATE DATABASE Employee"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)


def show_databases_querey():
    try:
        connection = c.connect(host='localhost',
        user='root',
        password='Yasin@786'
        )
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
    except Exception as e:
        print(e)


def create_table_query():
    try:
        connection = c.connect(host='localhost',
        user='root',
        password='Yasin@786',
        database = 'Employee'
        )
        create_table_query = """
        CREATE TABLE Employee_info(
            id int auto_increment,
            name varchar(50),
            work_exp varchar(50),
            joining_date date, primary key(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

def show_table_query():
    try:
        connection = c.connect(host='localhost',
           user='root',
           password='Yasin@786',
           database='Employee'
           )
        show_table_query = "DESCRIBE Information_Employee" #"DESCRIBE Employee_info"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            # print(result)
            for row in result:          # Fetch rows from last executed query
                print(row)
    except Exception as e:
        print(e)


def adding_new_column():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        alter_table_query = """
            ALTER TABLE Employee_info
            add column address varchar(50)
         """
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
    except Exception as e:
        print(e)


def remove_column_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Employee'
                           )
    alter_table_query = """
            ALTER TABLE Employee_info
            drop address;
         """
    with connection.cursor() as cursor:
        cursor.execute(alter_table_query)
        connection.commit()


def update_column_name_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Employee'
                           )
    alter_table_query = """
        ALTER TABLE Employee_info
        rename column joining_date to date_of_joining
     """
    show_table_query = "DESCRIBE Employee_info"
    with connection.cursor() as cursor:
        cursor.execute(alter_table_query)
        cursor.execute(show_table_query)
        res = cursor.fetchall()
        print(res)

def insert_after_column_query():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        alter_table_query = """
           ALTER TABLE Employee_info 
           add last_name varchar(40) NOT NULL after name;
         """
        show_table_query = "DESCRIBE Employee_info"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

def update_table_name_query():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        alter_main_table_query = """
            ALTER TABLE Employee_info
            rename to Information_Employee
         """
        show_table_query = "DESCRIBE Information_Employee"
        with connection.cursor() as cursor:
            cursor.execute(alter_main_table_query)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

# DML queries
def insert_data_to_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        work_exp = float(input('Enter experience: '))
        date_of_joining = input('Enter joining date: ')
        insert_data = 'INSERT INTO Information_Employee(name,last_name, work_exp, date_of_joining) values(%s, %s ,%s , %s)'
        data_value = (name, last_name, work_exp, date_of_joining)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)


def update_query_inside_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        last_name = input("Enter last name: ")
        work_exp = float(input('Enter experience'))
        joining_date = input('Enter joining date: ')
        update_data = 'UPDATE Information_Employee set name=%s,last_name=%s, work_exp=%s, date_of_joining=%s where id=%s'
        data_value = (name, last_name, work_exp, joining_date, id)
        conn = connection.cursor()
        conn.execute(update_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)


def delete_query_in_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        delete_query = "DELETE FROM Information_Employee WHERE id=%s and name=%s"
        connection.cursor()
        data_value = (id, name)
        conn = connection.cursor()
        conn.execute(delete_query, data_value)
        connection.commit()
    except Exception as e:
        print(e)


def display_table_info():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employee'
                               )
        select_table = "SELECT * FROM Information_Employee"
        with connection.cursor() as cursor:
            cursor.execute(select_table)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # mysql_connection()
    # show_databases_querey()
    # create_table_query()
    # adding_new_column()
    # remove_column_query()
    # update_column_query()
    # insert_after_column_query()
    # update_table_name_query()
    # show_table_query()

    # dml
    insert_data_to_table()
    # update_query_inside_table()
    # delete_query_in_table()
    # display_table_info()
