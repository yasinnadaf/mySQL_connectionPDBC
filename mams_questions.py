import mysql.connector as c

def create_database():
    try:
        connection = c.connect(host = 'localhost',
        user = 'root',
        password = 'Yasin@786'
        )
        create_db_query = "CREATE DATABASE Assignment_m"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)


def create_table_query():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database = 'Assignment_m'
        )
        create_table_query = """
        CREATE TABLE Employees(
            emp_id int auto_increment,
            first_name varchar(50),
            last_name varchar(50),
            work_exp varchar(50),
            salary int,
            primary key(emp_id)
        )
    """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

def insert_data_to_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='Assignment_m'
                               )
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        work_exp = float(input('Enter experience: '))
        salary = int(input('Enter salary: '))
        insert_data = 'INSERT INTO Employees(first_name,last_name, work_exp, salary) values(%s, %s ,%s , %s)'
        data_value = (first_name,last_name, work_exp, salary)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

#1
def get_char():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    query_to_get_char = 'select substring(first_name, 1, 3) from Employees'
    cursor = connection.cursor()
    cursor.execute(query_to_get_char)
    res = cursor.fetchall()
    for row in res:
        print(row)

#2
def get_full_names():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    get_full_name = 'select CONCAT("",first_name, last_name) from Employees'
    cursor = connection.cursor()
    cursor.execute(get_full_name)
    res = cursor.fetchall()
    for row in cursor:
        print(row)

#3
def length_of_fname_lname():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    length_of_names = 'SELECT first_name,last_name, LENGTH(first_name)+LENGTH(last_name)  "Length of Names" FROM Employees;'
    select_query = 'select * from Employees'
    cursor = connection.cursor()
    cursor.execute(length_of_names)
    cursor.execute(select_query)
    res = cursor.fetchall()
    for row in cursor:
        print(row)

#4
def check_number_in_field():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    num_in_fields = 'SELECT * from Employees where first_name regexp"[0-9]"'
    cursor = connection.cursor()
    cursor.execute(num_in_fields)
    res = cursor.fetchall()
    for row in cursor:
        print(row)

#5
def monthly_salary():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    round_monthly_salary = 'SELECT first_name, last_name, round(salary/12, 2) as "monthly_salary" from Employees'
    cursor = connection.cursor()
    cursor.execute(round_monthly_salary)
    res = cursor.fetchall()
    for row in cursor:
        print(row)

def display_table_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Assignment_m'
                           )
    select_table_query = "select * from Employees"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

if __name__ == '__main__':
    # create_database()
    # create_table_query()
    # insert_data_to_table()
    # display_table_query()

    #1
    # get_char()
    #2
    # get_full_names()
    #3
    # length_of_fname_lname()
    #4
    # check_number_in_field()
    #5
    monthly_salary()