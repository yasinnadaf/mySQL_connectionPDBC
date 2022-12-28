import mysql.connector as c

def mysql_connection():
    try:
        connection = c.connect(host = 'localhost',
        user = 'root',
        password = 'Yasin@786'
        )
        create_db_query = "CREATE DATABASE Employees"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)


def create_table_query():
    try:
        connection = c.connect(host='localhost',
        user='root',
        password='Yasin@786',
        database = 'Employees'
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

# DML queries
def insert_data_to_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Employees'
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
                               database='Employees'
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
                               database='Employees'
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
                               database='Employees'
                               )
        select_table = "SELECT * FROM Information_Employees"
        with connection.cursor() as cursor:
            cursor.execute(select_table)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # mysql_connection()
    # create_table_query()
    insert_data_to_table()
    # update_query_inside_table()
    # delete_query_in_table()
    display_table_info()

