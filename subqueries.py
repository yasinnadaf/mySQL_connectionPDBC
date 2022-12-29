import mysql.connector as c

def create_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database = 'Departments'
                           )
    create_table_query ="""
    CREATE TABLE emp_table(
            emp_id int auto_increment,
            name varchar(50),
            age int,
            gender varchar(10),
            dept varchar(50),
            salary int,
            city varchar(50), primary key(emp_id)
        )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)

def insert_into_table():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))
    city = input("Enter city: ")
    insert_data = 'INSERT INTO emp_table(name, age, gender, dept, salary, city) values(%s ,%s, %s, %s ,%s, %s)'
    data_value = (name, age, gender, dept, salary, city)
    conn = connection.cursor()
    conn.execute(insert_data, data_value)
    connection.commit()

# ex1 max salary
def max_salary():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    subquery_for_max_salary = 'select dept from emp_table where salary=(select max(salary) from emp_table)'
    cursor = connection.cursor()
    cursor.execute(subquery_for_max_salary)
    res = cursor.fetchall()
    for row in res:
        print(row)


def min_salary_dept():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    subquery_for_max_salary = 'select dept from emp_table where salary=(select min(salary) from emp_table)'
    cursor = connection.cursor()
    cursor.execute(subquery_for_max_salary)
    res = cursor.fetchall()
    for row in res:
        print(row)

def second_higest_salary():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    subquery_for_2ndmax_salary = 'select max(salary) from emp_table where salary < (select max(salary) from emp_table)'
    cursor = connection.cursor()
    cursor.execute(subquery_for_2ndmax_salary)
    res = cursor.fetchall()
    for row in res:
        print(row)


def update_subquery():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    subquery_update = 'update emp_table set salary=salary*2 where age in (select age from emp_table where age >= 22)'
    cursor = connection.cursor()
    cursor.execute(subquery_update)
    res = cursor.fetchall()
    for row in res:
        print(row)

def delete_subquery():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    delete_subquery = 'delete from emp_table where salary=(select from emp_table where max(salary))'
    cursor = connection.cursor()
    cursor.execute(delete_subquery)
    res = cursor.fetchall()
    for row in res:
        print(row)

def display_table_query():
    connection = c.connect(host='localhost',
                           user='root',
                           password='Yasin@786',
                           database='Departments'
                           )
    select_table_query = "select * from emp_table"
    with connection.cursor() as cursor:
        cursor.execute(select_table_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

if __name__ == '__main__':
    # create_table()
    # insert_into_table()
    display_table_query()

    #ex1
    # max_salary()
    #2
    # min_salary_dept()
    #3
    second_higest_salary()
    # ex4
    # update_subquery()
    #ex5
    # delete_subquery()
