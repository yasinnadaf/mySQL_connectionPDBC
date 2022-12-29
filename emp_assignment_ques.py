import mysql.connector as c


def create_database():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               )
        create_db_query = "CREATE DATABASE employee_data"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)

# 8
def create_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        create_table_query = """
           CREATE TABLE employees(
               employee_id int auto_increment,
               first_name varchar(50),
               last_name varchar(50),
               phone_number int,
               email varchar(30),
               hire_date DATE,
               job_id int,
               salary int,
               commission DECIMAL,
               manager_id int,
               department_id int,
               UNIQUE(employee_id)
           )
            """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

# 9
def change_column():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )

        alter_table_column_name = """
                                    UPDATE employees SET email='not available',
                                    commission=0.10
                              """
        show_table_query = "DESCRIBE employees"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_column_name)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

# 10
def insert_values():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        first_name = input("Enter name: ")
        last_name = input("Enter last name: ")
        phone_number = int(input("Enter phone number: "))
        email = input("Enter email: ")
        hire_date = input('Enter hire date: ')
        job_id = int(input("Enter job id: "))
        salary = int(input("Enter salary: "))
        commission = float(input("Enter commission"))
        manager_id = int(input("Enter manager id: "))
        department_id = int(input("Enter department id: "))
        insert_data = 'INSERT INTO employees(first_name,last_name,  phone_number, email, hire_date, job_id,' \
                      'salary, commission, manager_id, department_id) values(%s, %s ,%s , %s, %s, %s ,%s ,%s, %s, %s)'
        data_value = (first_name, last_name, phone_number, email, hire_date, job_id, salary, commission,
                      manager_id, department_id)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

# 10
def change_salary():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        updating_set_query = "UPDATE employees SET salary = 8000 WHERE employee_id = 2 AND salary < 5000;"
        show_table_query = "select * from employees"
        with connection.cursor() as cursor:
            cursor.execute(updating_set_query)
            cursor.execute(show_table_query)
            res = cursor.fetchall()
            print(res)
    except Exception as e:
        print(e)

# 11
def query_for_unique_department():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        unique_set_query = "SELECT DISTINCT department_id FROM employees;"
        show_table_query = "select * from employees"
        cursor = connection.cursor(buffered=True)
        cursor.execute(unique_set_query)
        cursor.execute(show_table_query)
        res = cursor.fetchall()
        print(res)
    except Exception as e:
        print(e)

# 12
def get_emp_orderby_desc():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        order_by_query = "SELECT * from employees order by first_name desc"
        show_table_query = "select * from employees"
        cursor = connection.cursor(buffered=True)
        cursor.execute(order_by_query)
        cursor.execute(show_table_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 13
def avg_salary():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        order_by_query = "SELECT AVG(salary), COUNT(*) FROM employees"
        show_table_query = "select * from employees"
        cursor = connection.cursor()
        cursor.execute(order_by_query)
        cursor.execute(show_table_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 14
def first_five_records():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        order_by_query = "SELECT * FROM employees where employee_id limit 5"
        cursor = connection.cursor()
        cursor.execute(order_by_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 15
def weekday():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        day_name_query = "SELECT distinct(yearweek(hire_date, 1)) from employees"
        cursor = connection.cursor()
        cursor.execute(day_name_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(a)

# 16
def last_day_of_current_yr():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        day_name_query = " SELECT DATE_FORMAT(NOW(),'%Y-12-31')"
        cursor = connection.cursor()
        cursor.execute(day_name_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 17
def fname_and_hire_date():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        day_name_query = "SELECT first_name, hire_date from employees where hire_date between '2020-02-22' and '2021-09-08'"
        cursor = connection.cursor()
        cursor.execute(day_name_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 18
def fname_lname_in_june():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        fl_name_query = "SELECT first_name, last_name from employee where month(hire_date, 6)"
        cursor = connection.cursor()
        cursor.execute(fl_name_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

# 20
def query_to_get_id_year():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        day_name_query = "SELECT count(employee_id) from employees where department_id and hire_date "
        cursor = connection.cursor()
        cursor.execute(day_name_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
    except Exception as e:
        print(e)

def show_tables():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='employee_data'
                               )
        show_table_query = "select * from employees"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # create_database()
    # create_table()
    # insert_values()
    #10
    # change_salary()
    #11
    # query_for_unique_department()
    # show_tables()
    # change_column()
    # 12
    # get_emp_orderby_desc()
    # 13
    # avg_salary()
    # show_tables()
    # 14
    # first_five_records()
    # 15
    # weekday()
    # 16
    # last_day_of_current_yr()
    # 17
    # fname_and_hire_date()
    # 18
    # fname_and_hire_date()
    # 20
    query_to_get_id_year()
