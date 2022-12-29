import mysql.connector as c


def create_database():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           )
    create_db_query = "CREATE DATABASE Company_1"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)

def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'Company_1'
                           )
    create_table_query ="""
    CREATE TABLE Employee(
             id INT auto_increment,
             name VARCHAR(45) NOT NULL,
             department VARCHAR(45) NOT NULL,
             salary int NOT NULL,
             gender VARCHAR(45) NOT NULL,
             age INT NOT NULL,
             city VARCHAR(45) NOT NULL, primary key(id)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Company_1'
                           )
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    insert_data = 'INSERT INTO Employee(name, department, salary, gender, age, city) values(%s ,%s, %s, %s ,%s, %s)'
    data_value = (name, department, salary, gender, age, city)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Company_1'
                           )
    select_table_query = "select * from Employee"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

# 2table
def create_table_2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'Company_1'
                           )
    create_table_query ="""
    CREATE TABLE Projects(
             project_id INT auto_increment,
            title VARCHAR(200) NOT NULL,
            client_id INT,
            employee_id INT,
            start_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            end_date DATE,
            FOREIGN KEY (employee_id) REFERENCES Employee(id),
            PRIMARY KEY(project_id)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_values_2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Company_1'
                           )
    title = input("Enter title: ")
    client_id = int(input("Enter client id: "))
    employee_id = int(input("Enter employee id: "))
    end_date = input("Enter end date: ")
    insert_data = 'INSERT INTO Projects(title, client_id, employee_id, end_date) values(%s, %s ,%s, %s)'
    data_value = (title, client_id, employee_id, end_date)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

def display_table_query_2():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Company_1'
                           )
    select_table_query = "select * from Projects"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)


if __name__ == '__main__':
    # create_database()
    # create_table()
    # insert_values()
    # display_table_query()

    # create_table_2()
    # insert_values_2()
    display_table_query_2()
