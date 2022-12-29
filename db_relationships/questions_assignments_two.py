import mysql.connector as c


def create_database():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               )
        create_db_query = "CREATE DATABASE assignment"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
    except Exception as e:
        print(e)

# 1
def create_table_1():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database = 'assignment'
                               )
        create_table_query ="""
        CREATE TABLE job_histry(
                employee_id int auto_increment, 
                start_date datetime DEFAULT CURRENT_TIMESTAMP, 
                end_date DATE, 
                job_id int , 
                department_id int, primary key(employee_id) 
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)

def insert_into_table_1():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        end_date = input("Enter end date: ")
        job_id = int(input("Enter job id: "))
        department_id = int(input("Enter department id: "))
        insert_data = 'INSERT INTO job_histry(end_date, job_id, department_id) values(%s ,%s, %s)'
        data_value = (end_date, job_id, department_id)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)


def select_query_1():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        select_table_query = "select * from job_histry"
        with connection.cursor() as cursor:
            cursor.execute(select_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)


# ques2
def create_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database = 'assignment'
                               )
        create_table_query ="""
        CREATE TABLE jobs(
                employee_id int , 
                start_date datetime DEFAULT CURRENT_TIMESTAMP, 
                end_date DATE, 
                job_id int auto_increment, 
                unique(job_id),
                department_id int, primary key(job_id) 
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)


def insert_into_table():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        employee_id = int(input("Enter employee id: "))
        end_date = input("Enter end date: ")
        department_id = int(input("Enter department id: "))
        insert_data = 'INSERT INTO jobs(employee_id, end_date, department_id) values(%s ,%s, %s)'
        data_value = (employee_id, end_date, department_id)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

def select_query():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        select_table_query = "select * from jobs"
        with connection.cursor() as cursor:
            cursor.execute(select_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

# 3
def create_table_2():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database = 'assignment'
                               )
        create_table_query ="""
        CREATE TABLE job_history(
                employee_id int auto_increment , 
                start_date datetime DEFAULT CURRENT_TIMESTAMP, 
                end_date DATE, 
                job_id int, 
                department_id int, primary key(employee_id),
                FOREIGN KEY (job_id) REFERENCES jobs(job_id) 
            )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
    except Exception as e:
        print(e)


def insert_into_table_2():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        end_date = input("Enter end date: ")
        job_id = int(input("Enter job id: "))
        department_id = int(input("Enter department id: "))
        insert_data = 'INSERT INTO job_history(end_date, job_id, department_id) values(%s ,%s, %s)'
        data_value = (end_date, job_id, department_id)
        conn = connection.cursor()
        conn.execute(insert_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

def select_query_2():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        select_table_query = "select * from job_history"
        with connection.cursor() as cursor:
            cursor.execute(select_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

# 3
def insert_row_in_job_histry():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        end_date = input("Enter end date: ")
        job_id = int(input("Enter job id: "))
        department_id = int(input("Enter department id: "))
        insert_row_data = 'INSERT INTO jobs(end_date, job_id, department_id) values(%s ,%s, %s)'
        data_value = (end_date, job_id, department_id)
        conn = connection.cursor()
        conn.execute(insert_row_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

# 4
def insert_rows_job_history():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        end_date = input("Enter end date: ")
        job_id = int(input("Enter job id: "))
        department_id = int(input("Enter department id: "))
        insert_rows_data = 'INSERT INTO job_history(end_date, job_id, department_id) values(%s ,%s, %s)'
        data_value = (end_date, job_id, department_id)
        conn = connection.cursor()
        conn.execute(insert_rows_data, data_value)
        connection.commit()
    except Exception as e:
        print(e)

# 5
def add_foreign():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        add_foreign_key = 'ALTER TABLE job_history ADD CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id) '
        show_table_query = "select * from job_history"
        with connection.cursor() as cursor:
            cursor.execute(add_foreign_key)
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

# 6
def drop_existing_foreign_key():
    try:
        connection = c.connect(host='localhost',
                               user='root',
                               password='Yasin@786',
                               database='assignment'
                               )
        add_foreign_key = 'alter table job_history drop foreign key fk_job_id'
        with connection.cursor() as cursor:
            cursor.execute(add_foreign_key)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # create_database()
    # create_table_1()
    # insert_into_table_1()
    select_query_1()

    # create_table()
    # insert_into_table()
    # select_query()

    # create_table_2()
    # insert_into_table_2()
    # select_query_2()
    #3
    # insert_row_in_job_histry()

    #4
    # insert_rows_job_history()

    #5
    # add_foreign()

    #6
    # drop_existing_foreign_key()
